from jinja2 import *
from kirby.template.default_filters import filters

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{% for page in site.pages.values() %}
<url>
<loc>http://{{site.config.domain|escape}}{{page.url|escape}}</loc>
<lastmod>{{page.modified_at|datetimeformat("%Y-%m-%d")}}</lastmod>
{% if page.data.changefreq %}<changefreq>{{page.data.changefreq}}</changefreq>{% endif %}
{% if page.data.priority %}<priority>{{page.data.priority}}</priority>{% endif %}
</url>
{% endfor %}</urlset>"""

def sitemap(site):
    """Returns an XML sitemap for the site."""
    env = Environment()
    env.filters.update(filters)
    template = env.from_string(SITEMAP)
    return template.render(site=site).replace('\n', '')