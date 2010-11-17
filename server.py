from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import autoreload
from core import render_path

class NanookHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        body = render_path(self.path)
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
        server = HTTPServer(('', PORT), NanookHandler)
        print 'Nanook serving on port %s (^C to quit) ...' % PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print "Shutting down."
        server.socket.close()
        
if __name__ == '__main__':
    autoreload.main(_serve)