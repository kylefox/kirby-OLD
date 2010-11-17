import os
import yaml
import markdown
from jinja2 import *

from kirby import settings

class Page():
    
    def __init__(self, d):
        self.template = "page.html"
        self.data = d
        for p in d.keys():
            self.__dict__[p] = d[p]
            
    def render(self):
        env = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIRS))
        template = env.get_template(self.template)
        return template.render(self.data)

def parse(page):
    content = open(os.path.join(settings.CONTENT_DIR, page)).read()
    data = yaml.load(content)
    data['content'] = data['content'].replace('\n', '\n\n')
    data['content'] = markdown.markdown(data['content'])
    page = Page(data)
    return page.render()