from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Hello from Docker container"}')

    def log_message(self, format, *args):
        print(f"[LOG] {self.address_string()} - {format % args}")

server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Server running on port 5000...")
server.serve_forever()