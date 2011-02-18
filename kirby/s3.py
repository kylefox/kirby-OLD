import os
import mimetypes
import cStringIO, gzip
from boto.s3.connection import S3Connection
from boto.s3.key import Key

GZIP_CONTENT_TYPES = (
    'text/css',
    'text/html',
    'text/xml',
    "text/javascript",
    'application/javascript',
    'application/x-javascript'
)

class InvalidAWSCredentials(Exception):
  pass

def connect_s3(bucket_name):
    """
    Opens a connection to Amazon S3 and gets the KIRBY_BUCKET.
    Returns a tuple: (connection, bucket)
    """
    try:
      AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
      AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
      connection = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
      bucket = connection.get_bucket(bucket_name)
      return (connection, bucket)
    except KeyError:
      raise InvalidAWSCredentials("Missing Amazon AWS credentials.")

def _gzip(data):
    zbuf = cStringIO.StringIO()
    zfile = gzip.GzipFile(mode='wb', compresslevel=6, fileobj=zbuf)
    zfile.write(data)
    zfile.close()
    return zbuf.getvalue()
    
def expiry_date():
    from wsgiref.handlers import format_date_time
    from datetime import datetime, timedelta
    from time import mktime
    future_date = datetime.now() + timedelta(days=10 * 365)
    stamp = mktime(future_date.timetuple())
    return format_date_time(stamp)

def upload_to_s3(site, bucket_name):
    
    s3_connection, bucket = connect_s3(bucket_name)
    
    # Upload content
    print 'Uploading content...'
    for path, content in site.s3_page_dict().items():
        k = Key(bucket)
        k.key = path
        k.set_contents_from_string(_gzip(content), {'Content-Type': 'text/html', 'Content-Encoding': 'gzip'})
        k.set_acl('public-read')
    
    print "Uploading media..."
    for root, dirs, files in os.walk(site.media_path):
        headers = {'Expires': expiry_date()}
        for f in files:
            file_path = os.path.join(root, f)
            file_key = file_path.replace(site.root_path, '')[1:]
            file_data = open(file_path, 'rb').read()

            content_type = mimetypes.guess_type(file_path)[0]
            if content_type:
                headers['Content-Type'] = content_type
                
            if content_type in GZIP_CONTENT_TYPES:
                headers['Content-Encoding'] = 'gzip'
                file_data = _gzip(file_data)
                
            asset = Key(bucket)
            asset.key = file_key
            asset.set_contents_from_string(file_data, headers)
            asset.set_acl('public-read')

    print 'Done!'