from http.server import SimpleHTTPRequestHandler, HTTPServer

server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Servidor iniciado en http://localhost:8080")
server.serve_forever()
