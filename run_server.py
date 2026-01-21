#!/usr/bin/env python3
"""
Flappy Horse Game - Server Runner
This will start the server and show you exactly what to do.
"""
import os
import sys
import webbrowser
import http.server
import socketserver
import time
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()
os.chdir(SCRIPT_DIR)

PORT = 8000

print("=" * 70)
print("  FLAPPY HORSE GAME - SERVER STARTUP")
print("=" * 70)
print()
print(f"Script location: {__file__}")
print(f"Working directory: {os.getcwd()}")
print(f"Script directory: {SCRIPT_DIR}")
print()

# Verify files exist
files_to_check = ['index.html', 'Images']
all_exist = True

for item in files_to_check:
    path = SCRIPT_DIR / item
    exists = path.exists()
    status = "✓" if exists else "✗"
    print(f"{status} {item}: {path}")
    if not exists:
        all_exist = False

print()

if not all_exist:
    print("ERROR: Required files not found!")
    print("Make sure you're running this from the game folder.")
    input("Press Enter to exit...")
    sys.exit(1)

# Find free port
def find_free_port(start_port):
    import socket
    for port in range(start_port, start_port + 10):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

port = find_free_port(PORT)
if port is None:
    print(f"ERROR: No free ports found (tried {PORT}-{PORT+9})")
    input("Press Enter to exit...")
    sys.exit(1)

if port != PORT:
    print(f"Note: Port {PORT} was busy, using port {port} instead")

# Create custom handler that shows what it's serving
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SCRIPT_DIR), **kwargs)
    
    def log_message(self, format, *args):
        # Show requests in console
        print(f"[{self.address_string()}] {format % args}")

# Create server
try:
    handler = MyHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    httpd.allow_reuse_address = True
    
    url = f"http://localhost:{port}/index.html"
    root_url = f"http://localhost:{port}/"
    
    print("=" * 70)
    print("  SERVER STARTED SUCCESSFULLY!")
    print("=" * 70)
    print()
    print(f"Server is running on port {port}")
    print(f"Serving from: {SCRIPT_DIR}")
    print()
    print("URLs to try:")
    print(f"  Main game:  {url}")
    print(f"  Root (file list): {root_url}")
    print()
    print("Opening browser in 2 seconds...")
    print("Keep this window open while playing!")
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    print()
    
    time.sleep(2)
    
    # Try to open browser
    try:
        webbrowser.open(url)
        print("Browser opened!")
    except Exception as e:
        print(f"Could not open browser automatically: {e}")
        print(f"Please manually open: {url}")
    
    print()
    print("Server is ready! Waiting for requests...")
    print()
    
    # Serve forever
    httpd.serve_forever()
    
except OSError as e:
    print(f"ERROR: Could not start server: {e}")
    print("Port may be in use or blocked by firewall")
    input("Press Enter to exit...")
except KeyboardInterrupt:
    print()
    print()
    print("Server stopped by user.")
    print("Thanks for playing!")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
