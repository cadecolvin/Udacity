from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = b'''
                <html>
                <head><title>Hey!</title></head>
                <body>Hello World!</body>
                </html>
                '''

                self.wfile.write(output)
                print('GET "/hello" 200')

                return
            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = b'''
                <html>
                <head><title>Hey!</title></head>
                <body>Hola</body>
                </html>
                '''

                self.wfile.write(output)
                print('GET "/hello" 200')

                return
        except IOError:
            self.send_error(b'404 File not found')
            print('ERROR: 404')

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print('Starting server...')

        server.serve_forever()

    except KeyboardInterrupt:
        print('Stopping server...')
        server.socket.close()

if __name__ == '__main__':
    main()
