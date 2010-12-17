import os
import yaml
import markdown


def file_path_to_url(site, path):
    """
    Given a filesystem path to a page, returns the absolute URL.
    >>> file_path_to_url('/home/example.com/content/services/design.md')
    u'/services/design'
    """
    return path.replace(site.content_path, "").rstrip('.md')

class PageManager(object):
    
    def __init__(self, site):
        self.site = site
        self.pages = []
        for k, v in self.site.pages.iteritems():
            self.pages.append(v)

    def all(self):
        return self.pages

    def in_path(self, path):
        page_set = []
        for page in self.pages:
            if page.url.lstrip('/').startswith(path.lstrip('/')):
                page_set.append(page)
        return page_set

class Page(object):

    def __init__(self, site, file_path):
        """
        Initializes the page object with data loaded from a markdown file.
        """
        self.site = site
        self.template = "page.html"
        self.url = file_path_to_url(site, file_path)
        self.s3_key = self.url.lstrip('/')
        if self.url == '/index':
            self.url = '/'
            self.html_path = 'index.html'
        else:
            self.html_path = '%s/index.html' % self.url.lstrip('/')
        content = open(file_path).read()
        try:
            ym, md = content.split('- - -')
            self.raw_markdown = md
            self.data = yaml.load(ym)
        except ValueError:
            self.data = {}
            self.raw_markdown = content
        self.data['content'] = markdown.markdown(self.raw_markdown)
        for p in self.data.keys():
            self.__dict__[p] = self.data[p]
    
    def __repr__(self):
        return '<Page: %s>' % self.url