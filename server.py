#HTTP server - serves static files with no logging
import http.server
import socketserver
import multiprocessing

def run_server(port):
    class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    with socketserver.TCPServer(("", port), NoCacheHTTPRequestHandler) as httpd:
        httpd.serve_forever()

def start_server(port):
    server_process = multiprocessing.Process(target=run_server, args=(port,))
    server_process.start()
    return server_process

def stop_server(server_process):
    if server_process and server_process.is_alive():
        server_process.terminate()
        server_process.join(timeout=2)
