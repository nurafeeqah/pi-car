import time
import RPi.GPIO as gpio
from libs.bcm_pin import BCM_PIN

class Ultrasonic:

    def __init__(self):

        # Set mode and warning
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Initialize pin
        bcmpin = BCM_PIN()
        self.ECHO = bcmpin.ECHO
        self.TRIG = bcmpin.TRIG

        # Ultrasonic pin
        gpio.setup(self.ECHO,gpio.IN)
        gpio.setup(self.TRIG,gpio.OUT)


    def getDistance(self):
        gpio.output(self.TRIG, False)                 #Set TRIG as LOW

        gpio.output(self.TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                           #Delay of 0.00001 seconds
        gpio.output(self.TRIG, False)                 #Set TRIG as LOW

        signal = 0
        nosignal   = 0
        speedConstant = 17150
        notInRange = 'Not in range'

        while gpio.input(self.ECHO)==0:               #Check whether the ECHO is LOW
            signal = time.time()                 #stores the last known time of LOW 

        while gpio.input(self.ECHO)==1:               #Check whether the ECHO is HIGH
            nosignal = time.time()                   #stores the last known time of HIGH  

        time = nosignal - signal             #Get  time to a variable

        distance = time * speedConstant             #time * speed = distance
        distance = round(distance, 2)                 #Round distance value to two decimal points

        if distance > 2 and distance < 400:           #Check whether the distance is in range
            print "Distance:",distance - 0.5,"cm"   #distance has 0.5 cm calibration
            return distance - 0.5
        else:
            return -1
            print notInRange                    #display not in range
