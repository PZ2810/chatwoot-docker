import http.server
import socketserver
import os

PORT = 4100
DIRECTORY = os.path.join(os.path.dirname(__file__), "public")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Allow embedding in Chatwoot iframes
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('X-Frame-Options', 'ALLOWALL')
        self.send_header('Content-Security-Policy', "frame-ancestors *")
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Admissions Dashboard running at http://0.0.0.0:{PORT}")
        httpd.serve_forever()
