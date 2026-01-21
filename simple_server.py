#!/usr/bin/env python3
"""
Simplest possible HTTP server for the game
"""
import os
import webbrowser
import http.server
import socketserver
import sys

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

# Try to find a free port
for port in range(8000, 8010):
    try:
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        httpd.allow_reuse_address = True
        
        current_dir = os.getcwd()
        print("=" * 60)
        print("  Flappy Horse Game Server")
        print("=" * 60)
        print(f"\nServing directory: {current_dir}")
        print(f"Server started on port {port}")
        print(f"\nAvailable files:")
        if os.path.exists('index.html'):
            print("  ✓ index.html found")
        else:
            print("  ✗ index.html NOT FOUND!")
        print(f"\nOpen in browser: http://localhost:{port}/index.html")
        print("Or try: http://localhost:{port}/ (to see directory listing)")
        print("\nPress Ctrl+C to stop")
        print("=" * 60)
        
        # Open browser
        url = f"http://localhost:{port}/index.html"
        webbrowser.open(url)
        
        # Serve forever
        httpd.serve_forever()
        break
    except OSError:
        if port == 8009:
            print(f"ERROR: Could not start server on ports 8000-8009")
            print("Please close other applications using these ports")
            input("Press Enter to exit...")
            sys.exit(1)
        continue
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        break
