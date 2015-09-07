import RPi.GPIO as gpio
from bcm_pin import BCM_PIN

class Motor:

    def __init__(self,speed=100):

        # Set mode and warning
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        # Initialize pin
        bcmpin = BCM_PIN()
        self.FRONT_1_PIN = bcmpin.FRONT_1
        self.FRONT_2_PIN = bcmpin.FRONT_2
        self.BACK_1_PIN = bcmpin.BACK_1
        self.BACK_2_PIN = bcmpin.BACK_2

        self.SPEED=speed

        gpio.setup(self.BACK_1_PIN, gpio.OUT)
        self.BACK_1=gpio.PWM(self.BACK_1_PIN, self.SPEED)
        self.BACK_1.start(0)

        gpio.setup(self.FRONT_1_PIN, gpio.OUT)
        self.FRONT_1=gpio.PWM(self.FRONT_1_PIN, self.SPEED)
        self.FRONT_1.start(0)

        gpio.setup(self.BACK_2_PIN, gpio.OUT)
        self.BACK_2=gpio.PWM(self.BACK_2_PIN, self.SPEED)
        self.BACK_2.start(0)

        gpio.setup(self.FRONT_2_PIN, gpio.OUT)
        self.FRONT_2=gpio.PWM(self.FRONT_2_PIN, self.SPEED)
        self.FRONT_2.start(0)

    #Defining forward function
    def forward(self):
        print "forward with speed " + str(self.SPEED)
        self.FRONT_1.ChangeDutyCycle(self.SPEED)
        self.FRONT_2.ChangeDutyCycle(self.SPEED)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(0)

    def reverse(self):
        print "reverse"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(self.SPEED)
        self.BACK_2.ChangeDutyCycle(self.SPEED)

    def turnleft(self):
        print "turn left"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(self.SPEED)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(0)

    def turnright(self):
        print "turn right"
        self.FRONT_1.ChangeDutyCycle(self.SPEED)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(0)

    def reverseleft(self):
        print "reverse to left"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(self.SPEED)

    def reverseright(self):
        print "reverse to right"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(self.SPEED)
        self.BACK_2.ChangeDutyCycle(0)

    def spinclockwise(self):
        print "spin clockwise"
        self.FRONT_1.ChangeDutyCycle(self.SPEED)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(self.SPEED)

    def spinanticlockwise(self):
        print "spin anti-clockwise"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(self.SPEED)
        self.BACK_1.ChangeDutyCycle(self.SPEED)
        self.BACK_2.ChangeDutyCycle(0)

    def stop(self):
        print "Stop"
        self.FRONT_1.ChangeDutyCycle(0)
        self.FRONT_2.ChangeDutyCycle(0)
        self.BACK_1.ChangeDutyCycle(0)
        self.BACK_2.ChangeDutyCycle(0)
        
    def setSpeed(self,speed):
        self.SPEED = speed
        