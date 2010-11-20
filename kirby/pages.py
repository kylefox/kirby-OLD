import os
import yaml
import markdown
from jinja2 import *

class PageManager(object):
    
    def __init__(self, site):
        self.site = site
        self.pages = []
        gen = os.walk(site.content_path)
        for each_tuple in gen:
            for fname in each_tuple[2]:
                self.pages.append(Page(self.site, os.path.join(each_tuple[0],fname)))

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
        self.url = file_path.replace(site.content_path, "").rstrip('.md')
        self.s3_key = self.url.lstrip('/')
        if self.url == '/index':
            self.url = '/'
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


    def render(self):
        """
        Renders out the page object to a template, and return the 
        resulting html. Pages will attempt to use `page.html` as the 
        template name which can be overridden in the markdown file.
        """
        from kirby.template.default_filters import filters
        env = Environment(loader=FileSystemLoader(self.site.template_path))
        env.filters.update(filters)
        template = env.get_template(self.template)
        return template.render({ 'page': self, 'pages': PageManager(self.site) })
    
    def __repr__(self):
        return '<Page: %s>' % self.url