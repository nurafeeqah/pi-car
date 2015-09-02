import picamera
import time
import os
from PIL import Image

class Camera:

    def __init__(self, resolution=(300, 225), filename='/home/pi/project/pi-car/images/snap.jpg'):
        self.filename = filename
        self.resolution = resolution

    def captureImage(self):

        # Remove existing image first
        # self.removeImage(self.filename)

        camera = picamera.PiCamera()
        camera.resolution = self.resolution
        # camera.start_preview()
        camera.capture(self.filename)
        camera.close()

        print "Image has been captured."

    def removeImage(self, filename):
        try:
            os.remove(filename)
        except OSError:
            pass

    # Return dictionary
    def getBrightest(self):

        pic = Image.open(self.filename)
        pic = pic.convert('RGB')

        width, height = self.resolution
        brightest   = 0.0
        brightest_x = 0.0
        brightest_y = 0.0
        sleep_time = 2

        for y in range(height):
            for x in range(width):
                pixelRGB = pic.getpixel((x,y))
                R,G,B = pixelRGB
                brightness = (0.3*R) + (0.59*G) + (0.11*B)
                if brightness > brightest:
                    brightest = brightness
                    brightest_x = x
                    brightest_y = y

        return {
            'x'   : brightest_x,
            'y'   : brightest_y,
            'val' : brightest
        }
        