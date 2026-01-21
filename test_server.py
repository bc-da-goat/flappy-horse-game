#!/usr/bin/env python3
"""
Test server with directory listing
"""
import os
import http.server
import socketserver
import webbrowser

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class DirectoryHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

try:
    handler = DirectoryHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    httpd.allow_reuse_address = True
    
    current_dir = os.getcwd()
    print("=" * 60)
    print("  Flappy Horse Game Server")
    print("=" * 60)
    print(f"\nServing from: {current_dir}")
    print(f"Server URL: http://localhost:{PORT}/")
    print(f"Game URL: http://localhost:{PORT}/index.html")
    
    # List files
    print("\nFiles in directory:")
    for f in os.listdir('.'):
        if os.path.isfile(f):
            print(f"  - {f}")
    
    print("\nOpening browser...")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    url = f"http://localhost:{PORT}/index.html"
    webbrowser.open(url)
    
    httpd.serve_forever()
    
except OSError as e:
    print(f"ERROR: {e}")
    print("Port 8000 may be in use. Try closing other applications.")
    input("Press Enter to exit...")
except KeyboardInterrupt:
    print("\n\nServer stopped.")
