#!/usr/bin/env python3
"""
Ultra-simple test server - just to verify files are accessible
"""
import os
import http.server
import socketserver
from pathlib import Path

# Get absolute path to script directory
script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)

print("=" * 70)
print("SIMPLE TEST SERVER")
print("=" * 70)
print(f"Script: {__file__}")
print(f"Directory: {script_dir}")
print(f"Current working dir: {os.getcwd()}")
print()

# List files
print("Files in directory:")
for f in sorted(os.listdir('.')):
    if os.path.isfile(f):
        size = os.path.getsize(f)
        print(f"  {f} ({size} bytes)")

print()
print("Checking index.html:")
if os.path.exists('index.html'):
    print("  ✓ index.html EXISTS")
    print(f"  Full path: {os.path.abspath('index.html')}")
else:
    print("  ✗ index.html NOT FOUND")

print()
print("=" * 70)
print("Starting server on http://localhost:8000")
print("Try: http://localhost:8000/index.html")
print("Press Ctrl+C to stop")
print("=" * 70)
print()

# Simple server
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8000), handler)
httpd.allow_reuse_address = True

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
