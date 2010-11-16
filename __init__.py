import os
from jinja2 import *
from markdown import markdown

ROOT = os.getcwd()

# Directory that stores Jinja templates.
TEMPLATE_DIRS = [os.path.join(ROOT, 'templates')]

# Directory that holds content (markdown files).
CONTENT_DIR = os.path.join(ROOT, 'content')

env = Environment(loader=FileSystemLoader(TEMPLATE_DIRS))


def compile_page(page, **options):
  template = env.get_template(options.get('template', "base.html"))
  content = open(os.path.join(CONTENT_DIR, "%s.md" % page)).read()
  return template.render(content=markdown(content))
  
print compile_page('index')

print compile_page('index', template='homepage.html')