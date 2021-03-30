#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522               #For this code to work corecly setting need to be changed on the pi
reader = SimpleMFRC522()
try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)                      #when card is detected it asks what you want to write to the pi,then it writes whatever is typed to the card
        print("Written")                        #prints written to let the user know that info has been written
finally:
        GPIO.cleanup()
