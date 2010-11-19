from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from kirby import autoreload
from kirby import settings
from kirby.core import Kirby
    
def runserver(path):
    kirby = Kirby(path) 
    
    class KirbyHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            body = kirby.render_path(self.path)
            if body is None:
                self.send_response(404)
                body = "Not found (404): %s\n" % self.path
            else:
                self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body)

    def _serve():
        PORT = 8000
        try:
            server = HTTPServer(('', PORT), KirbyHandler)
            print 'Kirby serving on port %s (^C to quit) ...' % PORT
            print 'TEMPLATE_DIRS = %s' % settings.TEMPLATE_DIRS
            print 'CONTENT_DIR = %s' % settings.CONTENT_DIR
            server.serve_forever()
        except KeyboardInterrupt:
            print "Shutting down."
            server.socket.close()
    
    autoreload.main(_serve)