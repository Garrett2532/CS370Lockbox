import RPi.GPIO as GPIO
import time
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 20) # GPIO 17 for PWM with 20Hz
p.start(1)

while True:
#    p.ChangeDutyCycle(0)
    text = input('Position:')
    if(text == 'min'):
        p.ChangeDutyCycle(1)
       # p.ChangeDutyCycle(0)
    elif(text == 'mid'):
        p.ChangeDutyCycle(3)
      #  p.ChangeDutyCycle(0)
    elif(text == 'max'):
        p.ChangeDutyCycle(5)
       # p.ChangeDutyCycle(0)
    elif(text == 'done'):
        p.stop()
        GPIO.cleanup()
        break
    else:
        continue
