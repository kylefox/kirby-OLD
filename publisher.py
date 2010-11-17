import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from core import Nanook

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
NANOOK_BUCKET = os.environ['NANOOK_BUCKET']

def publish():
    pages = Nanook().s3_page_dict()
    s3 = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = s3.get_bucket(NANOOK_BUCKET)
    headers = {
        'Content-Type': 'text/html'
    }
    for path, content in pages.items():
        k = Key(bucket)
        k.key = path
        k.set_contents_from_string(content, headers)
        k.set_acl('public-read')

if __name__ == "__main__":
    publish()