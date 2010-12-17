import os
import shutil
import unittest
import kirby
from kirby.core import Kirby
from kirby.publisher import publish
from kirby.pages import Page

class PublisherTest(unittest.TestCase):
    
    def setUp(self):
        self.KIRBY_ROOT = os.path.dirname(kirby.__file__)
        self.site = Kirby(os.path.join(self.KIRBY_ROOT, 'site_template'))
        self.index = Page(self.site, os.path.join(self.site.content_path, 'index.md'))
        self.page = Page(self.site, os.path.join(self.site.content_path, 'about.md'))
        self.nested_page = Page(self.site, os.path.join(self.site.content_path, 'posts', 'example-post.md'))
        self.output_path = os.path.join(os.path.dirname(__file__), '_public')
        publish(self.site, output_path=self.output_path)
        
    def test_index_file_exists(self):
        assert os.path.exists(os.path.join(self.output_path, self.index.html_path))

    def test_page_file_exists(self):
        assert os.path.exists(os.path.join(self.output_path, self.page.html_path))
        
    def test_nested_page_file_exists(self):
        os.path.join(self.output_path, self.nested_page.html_path)
        
    def tearDown(self):
        # Delete all the files/directories we just wrote.
        shutil.rmtree(self.output_path)
