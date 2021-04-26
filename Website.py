from http.server import BaseHTTPRequestHandler, HTTPServer
import scripts.ServoRunner as servo

import RPi.GPIO as GPIO             
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
import time

hostName = ""
hostPort = 7000
myServer = HTTPServer((hostName, hostPort), MyServer) #sets up the server

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
            servo.open()
            servo.close()
            GPIO.cleanup()
            myServer.server_close()
   def standard_out(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Open the file
        with open('www/index.html', 'rb') as file:
            self.wfile.write(file.read()) # Read the file and send the content

def run():
    #try:
    #    while(True):                                      #scans for the propper ID
    #       id, text = reader.read()
    #       time.sleep(.2)
    #       print(id)
    #       if(id == 786697983187):
    #             myServer.serve_forever()                 #open server if propper ID given
    #except KeyboardInterrupt:
    #    pass
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
    myServer.server_close()
    GPIO.cleanup()

if __name__ == '__main__':
    run()
