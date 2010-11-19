import os

ROOT = os.getcwd()

# Directory that stores Jinja templates.
TEMPLATE_DIRS = [os.path.join(ROOT, 'templates')]

# Directory that holds content (markdown files).
CONTENT_DIR = os.path.join(ROOT, 'content')