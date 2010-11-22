import boto
from boto.cloudfront import CloudFrontConnection

def create_bucket(name):
    conn = boto.connect_s3()
    bucket = conn.create_bucket(name)
    bucket.set_acl('public-read')
    return bucket
    
def create_distribution(bucket):
    conn = CloudFrontConnection()
    distro = conn.create_distribution(
        origin="%s.s3.amazonaws.com" % bucket.name,
        enabled=False,
        comment='Kirby site (%s)' % bucket.name,
        cnames=[bucket.name]
    )
    distro.update(default_root_object='index')
    distro.enable()
    return distro
    
def setup_cloud(domain):
    bucket = create_bucket(domain)
    return create_distribution(bucket)
