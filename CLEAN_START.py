#!/usr/bin/env python3
"""
CLEAN START - Kills old servers and starts fresh
"""
import os
import sys
import http.server
import socketserver
import webbrowser
import time
import subprocess
from pathlib import Path

# Get script directory
SCRIPT_DIR = Path(__file__).parent.absolute()
os.chdir(SCRIPT_DIR)

print("=" * 70)
print("  CLEAN SERVER START")
print("=" * 70)
print()

# Kill any Python servers on port 8000
print("Checking for existing servers on port 8000...")
try:
    result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    pids = []
    for line in lines:
        if ':8000' in line and 'LISTENING' in line:
            parts = line.split()
            if len(parts) > 4:
                pid = parts[-1]
                if pid.isdigit():
                    pids.append(pid)
    
    if pids:
        print(f"Found {len(pids)} process(es) using port 8000")
        for pid in set(pids):
            try:
                subprocess.run(['taskkill', '/F', '/PID', pid], 
                             capture_output=True)
                print(f"  Killed process {pid}")
            except:
                pass
        time.sleep(1)
    else:
        print("  No existing servers found")
except:
    print("  Could not check for existing servers (continuing anyway)")

print()

# Verify files
index_path = SCRIPT_DIR / "index.html"
if not index_path.exists():
    print(f"ERROR: {index_path} not found!")
    sys.exit(1)

print(f"✓ Script directory: {SCRIPT_DIR}")
print(f"✓ index.html found: {index_path}")
print()

# Start server
PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SCRIPT_DIR), **kwargs)
    
    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

try:
    httpd = socketserver.TCPServer(("", PORT), MyHandler)
    httpd.allow_reuse_address = True
    
    url = f"http://localhost:{PORT}/index.html"
    
    print("=" * 70)
    print("  SERVER READY!")
    print("=" * 70)
    print()
    print(f"Port: {PORT}")
    print(f"Directory: {SCRIPT_DIR}")
    print()
    print(f"Open in browser: {url}")
    print()
    print("Opening browser now...")
    print("Keep this window open!")
    print("Press Ctrl+C to stop")
    print("=" * 70)
    print()
    
    time.sleep(1)
    webbrowser.open(url)
    
    print("Server running. Waiting for requests...")
    print()
    
    httpd.serve_forever()
    
except OSError as e:
    print(f"ERROR: {e}")
    print("Try a different port or close other applications")
    input("Press Enter to exit...")
except KeyboardInterrupt:
    print("\n\nServer stopped.")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
