from libs.motor import Motor
from sensors.light import Light
from sensors.ultrasonic import Ultrasonic
from sensors.camera import Camera
from libs.bcm_pin import BCM_PIN
import os
import time
import datetime

class Main:

    def __init__(self):

        self.bcm_pin = BCM_PIN()

        # Initialize motor with speed, 0 => slowest, 100 => fastest
        self.motor = Motor(50)
        self.light = Light()
        self.ultrasonic = Ultrasonic()
        self.camera = Camera((120, 90))

    def start(self, condition=1):

        # self.printInfoStatus()
        
        switcher = {
            0: 'brightest',
            1: 'distance'
        }
        method = getattr(self, switcher[condition], lambda: 'nothing')
        method()

    def printInfoStatus(self):
        # os.system('clear')
        print "Info: ", datetime.datetime.now()
        print ""
        print "Light sensor: "
        print self.light.getSensorState(1)
        print self.light.getSensorState(2)
        print ""
        print "Ultrasonic Distance: " + str(self.ultrasonic.getDistance()) + "cm"

    def distance(self):
        distance = self.ultrasonic.getDistance()
        if  10 <= distance <= 20:
            self.motor.forward()
        elif 1 <= distance <= 5:
            self.motor.reverse()
        else:
            self.motor.stop()

    def brightest(self):
        self.motor.setSpeed(30)
        self.camera.captureImage()
        width, height = self.camera.resolution

        brightest = self.camera.getBrightest()

        # If brightest in left
        if brightest['x'] < ((width/2) - 25):
            self.motor.spinanticlockwise()

        # If brightest in right
        elif brightest['x'] > ((width/2) + 25):
            self.motor.spinclockwise()
        
        # If brightest in front
        else:
            self.motor.forward()

    def stop(self):
        self.motor.stop()
        self.bcm_pin.cleanup()
