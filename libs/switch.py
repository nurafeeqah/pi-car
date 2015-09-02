import RPi.GPIO as gpio
from bcm_pin import BCM_PIN

class Switch:

    def __init__(self):

        # Set mode and warning
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Initialize pin
        bcmpin = BCM_PIN()
        self.SWITCH = bcmpin.SWITCH

        gpio.setup(self.SWITCH, gpio.IN)


    def getSwitchState(self):
        return gpio.input(self.SWITCH)