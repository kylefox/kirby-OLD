from nanook import parser

class Nanook(object):

    def render_path(self, path):
        """
        Return HTML for a given a URL fragment (ex: /services/django).
        If that page doesn't exist, None is returned.
        """
        try:
            return {
                '/': parser.parse('index.md'),
                '/post' : parser.parse('posts/this_is_a_post.md'),
                '/favicon.ico': ''
            }[path]
        except KeyError:
            return None
        
    def s3_page_dict(self):
        """
        Returns a dictionary whose keys are the S3 bucket keys
        and values are the HTML to be written.
        """
        return {
         'index.html': self.render_path('/'),
         'about/index.html': self.render_path('/about'),
        }