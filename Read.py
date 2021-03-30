#!/usr/bin/env python

import RPi.GPIO as GPIO                 #for this code to work corectly setting on the pi need to be changed
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
        id, text = reader.read()        #read from card and print whatever is written on the card 
        print(id)
        print(text)
finally:
        GPIO.cleanup()
