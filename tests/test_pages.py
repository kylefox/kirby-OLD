import os
import unittest
import kirby
from kirby.core import Kirby
from kirby.pages import Page

class PageTest(unittest.TestCase):
    
    def setUp(self):
        self.KIRBY_ROOT = os.path.dirname(kirby.__file__)
        self.site = Kirby(os.path.join(self.KIRBY_ROOT, 'site_template'))
        self.index = Page(self.site, os.path.join(self.site.content_path, 'index.md'))
        self.page = Page(self.site, os.path.join(self.site.content_path, 'posts', 'example-post.md'))
        
    def test_page_url(self):
        self.assertEqual(self.page.url, '/posts/example-post')
        
    def test_index_url(self):
        self.assertEqual(self.index.url, '/')
        
    def test_page_s3_key(self):
        self.assertEqual(self.page.s3_key, 'posts/example-post')
        
    def test_index_s3_key(self):
        self.assertEqual(self.index.s3_key, 'index')

    def test_default_template(self):
        self.assertEqual(self.page.template, 'page.html')
        
    def test_custom_template(self):
        page = Page(self.site, os.path.join(self.site.content_path, 'blog.md'))
        self.assertEqual(page.template, 'blog.html')