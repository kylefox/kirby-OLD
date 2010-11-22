A tiny little Python app that compiles markdown + Jinja and uploads the resulting HTML to Amazon S3 + CloudFront.

_This is still in early proof-of-concept stages.  It's not recommended for production use just yet._

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

    $ kirby create example.com

which creates the resulting directory structure:

* example.com
  * content
  * media
  * templates
    
    
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

Publishing to CloudFront
------------------------

Once you're happy with the current state of your site, you can generate static HTML files and upload them to Amazon S3 using:

    $ kirby publish
    
Publishing requires these environment variables to be set:

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
