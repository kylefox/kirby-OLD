class Nanook(object):

    def render_path(self, path):
        """
        Return HTML for a given a URL fragment (ex: /services/django).
        If that page doesn't exist, None is returned.
        """
        try:
            menu = '<p><a href="/">home</a> | <a href="/about">about</a> | <a href="/newp">not found</a></p>'
            return {
                '/': '<h1>Homepage</h1> %s' % menu,
                '/about': '<h1>about</h1> %s' % menu,
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