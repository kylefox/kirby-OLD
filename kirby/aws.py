import boto

def create_bucket(name):
    conn = boto.connect_s3()
    bucket = conn.create_bucket(name)
    bucket.set_acl('public-read')
    bucket.configure_website(suffix='index.html', error_key="404.html")
    return bucket
