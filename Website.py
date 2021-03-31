from http.server import BaseHTTPRequestHandler, HTTPServer
import scripts.ServoRunner as servo

hostName = ""
hostPort = 9000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.standard_out()
    def do_POST(self):
        self.standard_out()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        pwd = post_data.decode().split("=")[-1]
        print(pwd)
        if pwd == 'turn':
            servo.test()
    def standard_out(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Open the file
        with open('www/index.html', 'rb') as file:
            self.wfile.write(file.read()) # Read the file and send the contents


myServer = HTTPServer((hostName, hostPort), MyServer)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
