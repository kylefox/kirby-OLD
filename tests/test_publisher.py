import os
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
        publish(self.site)
        
    def test_index_file_exists(self):
        assert os.path.exists(self.index.absolute_html_path)
        
    def tearDown(self):
        # Delete all the files/directories we just wrote.
        pass

    # def test_page_file_exists(self):
    #     assert os.path.exists(self.page.absolute_html_path)
    #     
    # def test_nested_page_file_exists(self):
    #     assert os.path.exists(self.nested_page.absolute_html_path)