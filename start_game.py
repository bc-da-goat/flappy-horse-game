#!/usr/bin/env python3
"""
Flappy Horse Game - Server Launcher
Just run this file to start the game server!
"""
import os
import sys
import webbrowser
import http.server
import socketserver
import time

# Change to the directory where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

def find_free_port(start_port=8000, max_attempts=10):
    """Find a free port starting from start_port"""
    import socket
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

def main():
    print("=" * 60)
    print("  FLAPPY HORSE GAME - SERVER")
    print("=" * 60)
    print()
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("ERROR: index.html not found!")
        print(f"Current directory: {os.getcwd()}")
        input("Press Enter to exit...")
        return
    
    # Find a free port
    port = find_free_port(PORT)
    if port is None:
        print(f"ERROR: Could not find a free port starting from {PORT}")
        input("Press Enter to exit...")
        return
    
    if port != PORT:
        print(f"Port {PORT} is in use, using port {port} instead")
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    httpd.allow_reuse_address = True
    
    url = f"http://localhost:{port}/index.html"
    
    print(f"Server starting on port {port}...")
    print(f"Serving directory: {os.getcwd()}")
    print()
    print("=" * 60)
    print(f"  Game URL: {url}")
    print("=" * 60)
    print()
    print("Opening game in your browser...")
    print("Keep this window open while playing!")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    # Small delay before opening browser
    time.sleep(0.5)
    
    # Open browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Could not open browser automatically: {e}")
        print(f"Please manually open: {url}")
    
    # Start server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        print("Thanks for playing!")
    except Exception as e:
        print(f"\nERROR: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
