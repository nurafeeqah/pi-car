# This file is used to quickly cleanup board from terminal
# > sudo python cleanup.py

from libs.bcm_pin import BCM_PIN

bcmpin = BCM_PIN(True)
bcmpin.cleanup()
