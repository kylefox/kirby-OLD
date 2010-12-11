# Basic example showing how to update a distribution's root object.
from boto.cloudfront import CloudFrontConnection

DIST_ID = "DISTRIBUTION_ID"
ROOT_OBJECT = 'index'

c = CloudFrontConnection()
dist = c.get_distribution_info(DIST_ID)
dist.update(default_root_object=ROOT_OBJECT)