import os

def publish(site, output_path=None):
    """
    Writes the site's rendered page HTMl to `output_path`.
    If no output_path is specified, `site.default_output_path` is used.
    """
    
    if output_path is None:
        output_path = site.default_output_path
    elif not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for path, content in site.html_page_dict().items():
        path = os.path.join(output_path, path)
        
        # Make intermediate directories if they don't exist.
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        html = open(path, 'wb')
        html.write(content)
        html.close()
