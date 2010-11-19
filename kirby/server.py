import os
import mimetypes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from kirby import autoreload
from kirby.core import Kirby
    
def runserver(path):
    kirby = Kirby(path) 
    
    class KirbyHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            """ 
              First check for static media
              Note that we are stripping the starting `/` off path
              to allow path joining.
            """
            path = os.path.join(kirby.root_path, self.path[1:])
            if os.path.isfile(path):
                mime = mimetypes.guess_type(path)[0]
                body = open(path).read()
                self.send_response(200)
                self.send_header('Content-type', mime)
            else:  
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
            print 'Kirby serving `%s` on port %s (^C to quit) ...' % (kirby, PORT)
            server.serve_forever()
        except KeyboardInterrupt:
            print "Shutting down."
            server.socket.close()
    
    autoreload.main(_serve)