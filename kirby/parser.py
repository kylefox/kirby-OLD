import os
import yaml
import markdown
from jinja2 import *

class Page():

  def __init__(self, site, page):
    """
    Initializes the pag object with data loaded from a
    markdown file.
    """
    self.site = site
    self.template = "page.html"
    content = open(os.path.join(self.site.content_path, page)).read()
    ym, md = content.split('- - -')
    data = yaml.load(ym)
    data['content'] = markdown.markdown(md)
    self.data = data
    for p in data.keys():
        self.__dict__[p] = data[p]
          
  def render(self):
    """
    Renders out the page object to a template, and return the 
    resulting html. Pages will attempt to use `page.html` as the 
    template name which can be overridden in the markdown file.
    """
    env = Environment(loader=FileSystemLoader(self.site.template_path))
    template = env.get_template(self.template)
    return template.render(self.data)