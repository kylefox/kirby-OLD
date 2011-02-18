A tiny little Python app that compiles [Markdown](http://daringfireball.net/projects/markdown/syntax) + [Jinja2](http://jinja.pocoo.org/) into static HTML and (optionally) uploads it to [Amazon S3](http://aws.amazon.com/s3/).

_Kirby is still in it's infancy.  Be aware that the API could change dramatically until the first release._

Installing
----------

Kirby is installable with pip (recommended):

    $ pip install git+git://github.com/kylefox/kirby.git
    
You can also clone the repository and install:

    $ git clone git://github.com/kylefox/kirby.git
    $ cd kirby
    $ python setup.py install
    
Creating a Kirby site
---------------------

You create a new Kirby site with

    $ kirby new example.com

which creates the resulting directory structure:

* example.com
  * _public
  * content
  * media
  * templates
  
Here is the purpose of each directory:

* **_public** contains your compiled Kirby site after you publish it.  You should not modify this folder's contents.
* **content** contains your Markdown files (pages & blog posts).
* **media** contains images, CSS, JavaScript, and other static media.
* **templates** contains your Jinja2 template files.

    
    
Running the development server
------------------------------

After creating your site, spark up the development server:

    $ cd example.com
    $ kirby serve
    
The development server compiles your markdown and templates on the fly.  This is useful while you're working on the site design and for previewing content.

Creating pages
--------------

A **Page** is simply a markdown file located inside the `content` directory.  The URL to the page is the file path (relative to `content`) with the .md extension stripped.

Some examples:

* `content/about.md` is served at **http://localhost:8000/about**
* `company/team/sammy.md` is be served at **http://localhost:8000/company/team/sammy**

The only exception to this convention is the index page:

* `content/index.md` is served at **http://localhost:8000/**
 
Template Context
----------------

Inside your templates you can access your page data through the `page` context object. This object contains all dynamic YAML fields from your markdown file, as well as a `content` field taken from all content after the `- - -` delimiter.

Some examples:

* `{{ page.title }}` is a string mapped from the YAML element `title: My Title`
* `{{ page.date }}` is date mapped from the YAML element `date: date: 2010-11-16`

With the exception being the content:

* `{{ page.content }}` contains the markdown-rendered HTML content of your page

Uploading to Amazon S3
----------------------

Once you're happy with the current state of your site, you can generate static HTML files and upload them to Amazon S3 using:

    $ kirby s3
    
Uploading to S3 requires these environment variables to be set:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `KIRBY_BUCKET`

Running Tests
-------------

We use [nose](http://somethingaboutorange.com/mrl/projects/nose/0.11.2/) to test Kirby:

    $ git clone git://github.com/kylefox/kirby.git
    $ cd kirby
    $ nosetests

Contributing
------------

Please fork and send pull requests.

If you want something to work on, see our [issues](https://github.com/kylefox/kirby/issues) list.  We can also use help with:

* Tests
* Documentation
* Template tags
    * Fetching content (ex: show 5 blog posts on homepage)
    * Site-wide variables (site name, admin email, etc).
