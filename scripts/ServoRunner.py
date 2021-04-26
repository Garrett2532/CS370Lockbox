import RPi.GPIO as GPIO  # Import GPIO to use button and Servo            
import time # time needed to auto close the safe after 5 seconds no button
servoPIN = 11 # Pin the servo is on
buttonPIN = 40 # Pin the Butto is on
wait_time = 5 # Time to wait untill auto close the safe
closed = 1 # widths of pluses that mean closed to the servo
opened = 5 # widths of pluses that mean open to the servo

GPIO.setmode(GPIO.BOARD)            #other GPIO mode was giving errors
GPIO.setup(servoPIN, GPIO.OUT)      # This sets up the Servo to get data out
GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # This sets up the button to send data in
p = GPIO.PWM(servoPIN, 20)          # sets up the servo GPIO pin 11 for PWM with 20Hz
p.start(closed)

def open():
    p.ChangeDutyCycle(opened)       # Sets the width to opened on the servo

def close():
    start_time = time.time()        # getting the intial time of calling closed which should be right after open
    while(True):                    # loop untill condition breaks from the waiting
        input_state = GPIO.input(buttonPIN) #scans for the push of a button that is connected to the pi
        if(input_state == False):           #button pressed
            p.ChangeDutyCycle(closed)       # closes the servo by setting the width to closed
            time.sleep(.7)                  # sleep for enough time to move the servo 
            break                           # Finished with the loop
        if(time.time()-start_time > wait_time):  # check if time elapsed is greater than the time set to wait
            p.ChangeDutyCycle(closed)       # closes the servo
            time.sleep(.7)                  # sleeps for the time needed to move the servo
            break                           # Finished the loop

def cleanup():
    p.stop()        # Stop the servo Runner
    GPIO.cleanup()  # Cleanup the pins used

# Code to test opening and closing with button
def test():
    setUp()

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
          

if __name__ == '__main__':
    test()
