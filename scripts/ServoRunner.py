import RPi.GPIO as GPIO             
import time
servoPIN = 11
buttonPIN = 40

def test():
    GPIO.setmode(GPIO.BOARD)            #other GPIO mode was giving errors
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    p = GPIO.PWM(servoPIN, 20) # GPIO 17 for PWM with 20Hz
    p.start(1)

    time.sleep(.5)                      #these values will need to be chnaged 
    p.ChangeDutyCycle(5)
    time.sleep(0.5)                     #will open the lock
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    
    while(True):
        input_state = GPIO.input(buttonPIN) #scans for the push of a button that is connected to the pi
        if(input_state == False):           #button pressed
            print("button working")
            time.sleep(.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)                 #these will need to be changed will lock the box
            p.ChangeDutyCycle(1)
            time.sleep(.5)
            time.sleep(0.2)
            p.stop()
            break
           # website.closeServer()
if __name__ == '__main__':
    test()
