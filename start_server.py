#!/usr/bin/env python3
"""
Simple HTTP server to run the Flappy Horse game in a browser
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

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
    # Change to the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("=" * 60)
    print("  Flappy Horse Game - Web Server")
    print("=" * 60)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("\nERROR: index.html not found!")
        print(f"Current directory: {os.getcwd()}")
        input("Press Enter to exit...")
        return
    
    # Find a free port
    port = find_free_port(PORT)
    if port is None:
        print(f"\nERROR: Could not find a free port starting from {PORT}")
        input("Press Enter to exit...")
        return
    
    if port != PORT:
        print(f"\nPort {PORT} is in use, using port {port} instead")
    
    Handler = MyHTTPRequestHandler
    
    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        httpd = socketserver.TCPServer(("", port), Handler)
        url = f"http://localhost:{port}/index.html"
        
        print(f"\nServer running at: {url}")
        print(f"Server directory: {os.getcwd()}")
        print("\nOpening game in your browser...")
        print("\nPress Ctrl+C to stop the server")
        print("=" * 60)
        
        # Small delay before opening browser
        import time
        time.sleep(0.5)
        
        # Open browser automatically
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Could not open browser automatically: {e}")
            print(f"Please manually open: {url}")
        
        httpd.serve_forever()
        
    except OSError as e:
        print(f"\nERROR: Could not start server: {e}")
        print(f"Port {port} may be in use or blocked by firewall")
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except Exception as e:
        print(f"\nERROR: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
