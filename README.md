A tiny little Python app that compiles markdown + Jinja and uploads the resulting HTML to Amazon S3/CloudFront
    
Ideal usage
------------

Create a project, S3 bucket and CloudFront distribution:

    $ nanook create example.com

Resulting directory structure:

    example.com/
    -- settings.py
    -- content/
    -- templates/
    
Running the local server:

    $ cd example.com
    $ nanook serve

Publishing to CloudFront:

    $ nanook publish
    
TODO
----

* Make nested pages (/about/design) work with CF.  Instead of naming keys "about/design/index.html" we could just name them "about/design".  (omit .html extension from S3 keys)
* Tests
* Documentation
* Static files (css/js/img): served from /media/
* Integrate LessCSS/YUICompressor
* Restructure codebase
    * work with pip
    * `nanook` should be normal python module.  It shouldn't be the root of all nanook sites.  Instead, _projects_ use the `nanook` module.
    * Create `bin/nanook` that handles the server, publishing, and creation of nanook projects.
* Template tags
    * Fetching content (ex: show 5 blog posts on homepage)
    * Site-wide variables (site name, admin email, etc).