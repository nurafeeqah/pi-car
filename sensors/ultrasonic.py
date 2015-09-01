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

        # Ultrasonic
        gpio.setup(self.ECHO,gpio.IN)
        gpio.setup(self.TRIG,gpio.OUT)


    def getDistance(self):
        gpio.output(self.TRIG, False)                 #Set TRIG as LOW
        # print "Waitng For Sensor To Settle"
        # time.sleep(2)                               #Delay of 2 seconds

        gpio.output(self.TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                           #Delay of 0.00001 seconds
        gpio.output(self.TRIG, False)                 #Set TRIG as LOW

        pulse_start = 0
        pulse_end   = 0

        while gpio.input(self.ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()                 #Saves the last known time of LOW pulse

        while gpio.input(self.ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                   #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start      #Get pulse duration to a variable

        distance = pulse_duration * 17150             #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)                 #Round to two decimal points

        if distance > 2 and distance < 400:           #Check whether the distance is within range
            # print "Distance:",distance - 0.5,"cm"   #Print distance with 0.5 cm calibration
            return distance - 0.5
        else:
            return -1
            # print "Out Of Range"                    #display out of range
