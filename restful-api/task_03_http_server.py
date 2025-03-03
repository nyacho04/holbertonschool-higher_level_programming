#!/usr/bin/python3

import http.server as srv
import socketserver
import json

PORT = 8000

class Server(srv.BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"Received GET request for {self.path}")
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jout = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(jout.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jout = json.dumps({"status": "OK"})
            self.wfile.write(jout.encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jout = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(jout.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            jout = json.dumps({"error": "Endpoint not found"})
            self.wfile.write(jout.encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Server) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()