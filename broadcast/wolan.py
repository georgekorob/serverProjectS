import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from wakeonlan import send_magic_packet


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        addr, port = self.client_address
        print(addr, port, self.path)
        data = self.path[1:]
        send_magic_packet(data)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Wolan get from {addr}:{port} to {data}".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        send_magic_packet(post_data)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Wolan for {post_data} success!".encode('utf-8'))


if __name__ == '__main__':
    addr = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    serv = HTTPServer((addr, port), HttpProcessor)
    serv.serve_forever()
