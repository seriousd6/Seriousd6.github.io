#!/usr/bin/env python3
"""Local dev server with cache disabled. Run from repo root: python3 scripts/serve.py"""
import http.server, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f'Serving at http://localhost:{PORT}  (Ctrl+C to stop)')
http.server.HTTPServer(('', PORT), NoCacheHandler).serve_forever()
