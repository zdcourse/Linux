import argparse
import os
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer

parser = argparse.ArgumentParser()
parser.add_argument("port", help="given the web service port", type=int)

args = parser.parse_args()
port = args.port
print(args.port)

content = '''
  <html>
      <body>
          <p>Hello World!</p>
          <p>{}</p>
          <p>{}</p>
      </body>
 </html>
'''


class myHandler(BaseHTTPRequestHandler):
    # handle the GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        msg1 = "Server: localhost: {}".format(port)
        msg2 = "Process ID: " + str(os.getpid())
        self.wfile.write(content.format(msg1, msg2))
        return


try:
    server = HTTPServer(('', port), myHandler)
    print 'Started httpserver on port: {}'.format(port)
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
