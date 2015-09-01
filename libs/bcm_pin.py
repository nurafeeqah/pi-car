import RPi.GPIO as gpio
import time

class BCM_PIN:

    def __init__(self, initOutput=False):

        # Use for motor
        self.FRONT_1        = 18  # OUT # LEFT
        self.FRONT_2        = 23  # OUT # RIGHT
        self.BACK_1         = 17  # OUT # LEFT
        self.BACK_2         = 22  # OUT # RIGHT

        # Use for ultrasonic
        self.TRIG           = 25  # OUT
        self.ECHO           = 24  # IN

        # Use for light sensor
        self.LIGHT_SENSOR_1 = 4   # IN
        self.LIGHT_SENSOR_2 = 27  # IN

        if initOutput:
            # Set mode and warning
            gpio.setmode(gpio.BCM)
            gpio.setwarnings(False)

            for pin in self.getOutPin():
                gpio.setup(pin,gpio.OUT)


    def getOutPin(self):
        return [
            self.FRONT_1, 
            self.FRONT_2, 
            self.BACK_1, 
            self.BACK_2,
            self.TRIG
        ]

    def cleanup(self):

        # Set mode and warning
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        for pin in self.getOutPin():
            gpio.output(pin, 0)

        time.sleep(0.5)
        gpio.cleanup()

        print "cleanup"