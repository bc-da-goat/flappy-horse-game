#!/usr/bin/env python3
"""
FIXED SERVER - This will definitely work!
"""
import os
import sys
import http.server
import socketserver
import webbrowser
import time
from pathlib import Path

# Force change to script directory
SCRIPT_FILE = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_FILE.parent
os.chdir(SCRIPT_DIR)

print("=" * 70)
print("  FLAPPY HORSE - FIXED SERVER")
print("=" * 70)
print()
print(f"Script file: {SCRIPT_FILE}")
print(f"Script directory: {SCRIPT_DIR}")
print(f"Current working directory: {os.getcwd()}")
print()

# Verify index.html
index_path = SCRIPT_DIR / "index.html"
print(f"Looking for index.html at: {index_path}")
if index_path.exists():
    print(f"✓ FOUND: {index_path}")
    print(f"  Size: {index_path.stat().st_size} bytes")
else:
    print(f"✗ NOT FOUND: {index_path}")
    print()
    print("ERROR: index.html not found!")
    print("Files in directory:")
    for f in sorted(SCRIPT_DIR.iterdir()):
        if f.is_file():
            print(f"  - {f.name}")
    input("\nPress Enter to exit...")
    sys.exit(1)

print()

# Try different ports
for port in [8000, 8001, 8002, 8003, 8004]:
    try:
        # Create handler that serves from script directory
        class MyHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=str(SCRIPT_DIR), **kwargs)
            
            def log_message(self, format, *args):
                # Log requests
                message = format % args
                print(f"[{self.address_string()}] {message}")
        
        httpd = socketserver.TCPServer(("", port), MyHandler)
        httpd.allow_reuse_address = True
        
        # Success!
        url = f"http://localhost:{port}/index.html"
        root_url = f"http://localhost:{port}/"
        
        print("=" * 70)
        print("  ✓ SERVER STARTED SUCCESSFULLY!")
        print("=" * 70)
        print()
        print(f"Port: {port}")
        print(f"Serving from: {SCRIPT_DIR}")
        print()
        print("URLs:")
        print(f"  Game:     {url}")
        print(f"  Root:     {root_url}")
        print(f"  Test:     {root_url}test_simple.py")
        print()
        print("Opening browser in 3 seconds...")
        print("Keep this window open!")
        print("Press Ctrl+C to stop")
        print("=" * 70)
        print()
        
        time.sleep(3)
        
        # Open browser
        try:
            webbrowser.open(url)
            print("Browser opened!")
        except:
            print(f"Please manually open: {url}")
        
        print()
        print("Server is running. Waiting for requests...")
        print()
        
        # Serve
        httpd.serve_forever()
        break
        
    except OSError as e:
        if port == 8004:
            print(f"ERROR: Could not start on any port (8000-8004)")
            print(f"Last error: {e}")
            input("Press Enter to exit...")
            sys.exit(1)
        continue
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        break
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")
        break
