#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import os
from pathlib import Path

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL path
        parsed_path = urllib.parse.urlparse(self.path)
        clean_path = parsed_path.path.lstrip('/')
        
        # Route mapping
        routes = {
            '': 'index.html',
            'strategy': 'strategy.html',
            'performance': 'performance.html',
            'team': 'team.html',
            'contact': 'contact.html',
            'fees': 'fees.html',
            'faq': 'faq.html',
            'legal/terms': 'legal/terms.html',
            'legal/privacy': 'legal/privacy.html',
            'legal/disclaimer': 'legal/disclaimer.html',
            'thank-you': 'thank-you.html'
        }
        
        # Check if it's a clean URL we need to route
        if clean_path in routes:
            # Redirect internally to the actual file
            self.path = '/' + routes[clean_path]
        elif clean_path.endswith('.html'):
            # Allow direct access to .html files
            pass
        elif clean_path and not clean_path.startswith('assets/') and not clean_path.startswith('css/') and not clean_path.startswith('js/'):
            # Unknown clean URL - try adding .html
            if os.path.exists(clean_path + '.html'):
                self.path = '/' + clean_path + '.html'
        
        # Call the parent handler
        super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    
    print(f"🚀 Starting server at http://localhost:{PORT}")
    print("📁 Serving from:", os.getcwd())
    print("\n🔗 Clean URLs enabled:")
    print("  http://localhost:8000/         → index.html")
    print("  http://localhost:8000/team     → team.html")
    print("  http://localhost:8000/strategy → strategy.html")
    print("  http://localhost:8000/contact  → contact.html")
    print("\n⏹️  Press Ctrl+C to stop")
    
    with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")