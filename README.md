# cs370_Final
Final project for cs370 written in python ran on RaspberryPi


To run the code ensure a servo controled by PWM with a pulse width of 20 ms is connected to pin 11. We reccomed the TIANKONGRC SG90. The code also requires a RFID scanner connected to the GPIO pins. The final reqirement is a button plugged into pin 40. After all these componets are attached download this code by running `git clone https://github.com/nd0905/cs370_Final.git`. After the files are downloaded run `python3 -m pip install -r requirements.txt && python3 Runner.py`. This will start running the code waiting for the RFID card to be scanned. After the tag is scanned go to `localhost:7000` and enter password `turn` to rotate the servo 90 degrees then back.
