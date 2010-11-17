import os
import yaml
from nanook import settings

class Page():
    
    def __init__(self, d):
        self.data = d
        for p in d.keys():
            self.__dict__[p] = d[p]
            
    def render(self):
        print "htmlz"

def Parse(page):
    content = open(os.path.join(settings.CONTENT_DIR, page)).read()
    data = yaml.load(content)
    page = Page(data)
    print page.date