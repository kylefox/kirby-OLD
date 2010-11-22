from jinja2 import *

from kirby.pages import PageManager
from kirby.template.default_filters import filters

def render(site, page):
    """
    Renders out the page object to a template, and return the 
    resulting html. Pages will attempt to use `page.html` as the 
    template name which can be overridden in the markdown file.
    """
    env = Environment(loader=FileSystemLoader(site.template_path))
    env.filters.update(filters)
    template = env.get_template(page.template)
    return template.render({ 'page': page, 'pages': PageManager(site) })