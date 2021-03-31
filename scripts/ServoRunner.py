import RPi.GPIO as GPIO
import time
servoPIN = 17

def test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 20) # GPIO 17 for PWM with 20Hz
    p.start(1)

    time.sleep(.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(1)
    time.sleep(.5)

    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    test()
