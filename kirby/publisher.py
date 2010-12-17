import os

def publish(site):
    
    for path, content in site.html_page_dict().items():
        # Make intermediate directories if they don't exist.
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        html = open(path, 'wb')
        html.write(content)
        html.close()
