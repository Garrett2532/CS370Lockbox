from http.server import BaseHTTPRequestHandler, HTTPServer # Import HTTP servers to run website
import scripts.ServoRunner as servo   # Import script to open and close the safe door

import RPi.GPIO as GPIO  # GPIO to ineract with servo button and RFID reader
from mfrc522 import SimpleMFRC522 # Package for RFID reader
reader = SimpleMFRC522()   # Set up the reader for RFID tag
import time   # needed for sleeping to add time for io

hostName = "" # Address HTTPServer will listen to "" for all addresses
hostPort = 7000 # Port server will listen on
password = 'turn' # password for opening the safe
running = True # Holds if the webserver is running or not

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.standard_out() # Handle a get request with the basic output page

    def do_POST(self):
        global running # needed to make sure it is changing the global variable and not a local one
        content_length = int(self.headers['Content-Length']) # get the content from a post request
        post_data = self.rfile.read(content_length) # read the bytes that came in from the post
        pwd = post_data.decode().split("=")[-1] # split off unneeded data  to get the password
        if pwd == password:
            self.success_pwd() # give webpage showing success password safe opening
            servo.open() # open the servo
            servo.close() # close the servo (this is a looping function so it might hang)
            running = False # Server can now shutdown
        else:
            self.failed_pwd() # similar to standard out but change index to a failed password page

    def failed_pwd(self):
        self.send_response(401) # unauthorized and bad password
        self.send_header("Content-type", "text/html") # Still send a HTML page for a reattempt
        self.end_headers() # Done with headers
        # Open the file
        with open('www/failed.html', 'rb') as file:
            self.wfile.write(file.read()) # Read the file and send the content
    def success_pwd(self):
        self.send_response(200) # success safe opening
        self.send_header("Content-type", "text/html") # send a html file to show safe opening
        self.end_headers() # Done with headers
        # Open the file
        with open('www/success.html', 'rb') as file:
            self.wfile.write(file.read()) # Read the file and send the content
    def standard_out(self):
        self.send_response(200) # sucess got to the website
        self.send_header("Content-type", "text/html") # send HTML page
        self.end_headers() # dont with header
        # Open the file
        with open('www/index.html', 'rb') as file:
            self.wfile.write(file.read()) # Read the file and send the content

myServer = HTTPServer((hostName, hostPort), MyServer) #sets up the server

def run_forever(): # Holds custom run_forever for my sever that will stop after successful post or 10 min
    global running # ensure using global varaible
    start_time = time.time() # get the starting time of the website
    while running:
        myServer.handle_request() # handle one request to the webserver
        if (time.time() - start_time > 600): # check current time after each request to make sure it has not been more than 10 min
            running = False

def run():
    global running # ensure using global variable
    try:                                                # Try to run this forever unless something stops it 
        while(True):                                      #scans for the propper ID
           id, text = reader.read()                     # read the reader to get the id from the RFID tag
           time.sleep(.2)                               # wait for it to clear the buffer
           if(id == 786697983187):                      # if ID is correct
               running = True                           # webserver can run now that it has proper authentication
               run_forever()                            # homemade run_forever for the website
    except KeyboardInterrupt:                           # if the keyboard sends interupt then end it
        pass
    myServer.server_close()                             # stop the server if its running
    servo.cleanup()
    GPIO.cleanup()                                      # clean up all GPIO

if __name__ == '__main__':                              # Run when called from CLI
    run()                                               # go into run fuction
