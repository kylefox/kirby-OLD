import os
import shutil
import kirby
from kirby.parser import Page

class Kirby(object):
    
    def __unicode__(self):
      return os.path.basename(self.root_path)
    
    def __repr__(self):
      return "<Kirby site: %s>" % unicode(self)
    
    @classmethod
    def create_site(self, root):
      """
      Creates a new Kirby site in `root` by copying the site_template.
      Returns the instantiated Kirby object.
      
      >>> Kirby.create_site('/home/kirby/example.com')
      <Kirby site: example.com>
      """
      shutil.copytree(os.path.join(kirby.__path__[0], 'site_template'), root)
      return self(root)
      
    @classmethod
    def reset_site(self, root):
         """
         Deletes the files in content, media, and template folders.
         Returns the instantiated Kirby object.
 
         >>> Kirby.reset_site('/home/kirby/example.com')
         <Kirby site: example.com>
         """
         site = Kirby(root)
         for path in 'content_path media_path template_path'.split():
             shutil.rmtree(getattr(site, path))
             os.mkdir(getattr(site, path))
    
    def __init__(self, root):
      self.root_path = root
      self.content_path = os.path.join(self.root_path, 'content')
      self.template_path = os.path.join(self.root_path, 'templates')
      self.media_path = os.path.join(self.root_path, 'media')
      self.reload_pages()
      
    def reload_pages(self):
        """
        Loads markdown files in the content directory.
        Returns a dictionary where keys are URLs and values are Page objects.
        """
        self.pages = {}
        for dirpath, dirnames, filenames in os.walk(self.content_path):
            for filename in filenames:
                if filename.endswith('.md'):
                    path = os.path.join(dirpath, filename)
                    page = Page(self, path)
                    self.pages[page.url] = page
    
    def render_path(self, path):
        """
        Return HTML for a given a URL fragment (ex: /services/django).
        If that page doesn't exist, None is returned.
        """
        try:
            return self.pages[path].render()
        except KeyError:
            return None
        
    def s3_page_dict(self):
        """
        Returns a dictionary whose keys are the S3 bucket keys
        and values are the HTML to be written.
        """
        pages = {}
        for page in self.pages.values():
            pages[page.s3_key] = page.render()
        return pages