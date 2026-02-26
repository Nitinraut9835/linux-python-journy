from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Backend is working")
        elif self.path == "/error":
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal Server Error")
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 5000), MyHandler)
print("Starting backend on port 5000...")
server.serve_forever()
