import RPi.GPIO as gpio
from libs.bcm_pin import BCM_PIN

class Light:

    def __init__(self):

        # Set mode and warning
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Initialize pin
        bcmpin = BCM_PIN()
        self.LIGHT_SENSOR_1 = bcmpin.LIGHT_SENSOR_1
        self.LIGHT_SENSOR_2 = bcmpin.LIGHT_SENSOR_2

        # set up digital line detectors as inputs
        gpio.setup(self.LIGHT_SENSOR_1, gpio.IN)
        gpio.setup(self.LIGHT_SENSOR_2, gpio.IN)


    def getSensorState(self, sensor_num):
        if sensor_num == 1:
            return gpio.input(self.LIGHT_SENSOR_1)
        elif sensor_num == 2:
            return gpio.input(self.LIGHT_SENSOR_2)
        else:
            return -1
