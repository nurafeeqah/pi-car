from motor import Motor
from sensor_light import Light
from sensor_ultrasonic import Ultrasonic
from bcm_pin import BCM_PIN
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

    def start(self):

        while(True):
            try:
                os.system('clear')
                print "Info: ", datetime.datetime.now()
                print ""
                print "Light sensor: "
                print self.light.getSensorState(1)
                print self.light.getSensorState(2)
                print ""
                print "Ultrasonic Distance: " + str(self.ultrasonic.getDistance()) + "cm"

                if self.ultrasonic.getDistance() > 15:
                    self.motor.forward()
                elif self.ultrasonic.getDistance() < 5:
                    self.motor.reverse()
                else:
                    self.motor.stop()

                time.sleep(0.2)

            except(KeyboardInterrupt):
                print "Finishing"
                self.stop()
                break

            except:
                print "Unexpected error"
                raise

    def stop(self):
        self.motor.stop()
        self.bcm_pin.cleanup()


main = Main()
main.start()

