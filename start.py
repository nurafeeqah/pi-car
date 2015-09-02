from libs.switch import Switch
from main import Main
import time

switch = Switch()
program = Main()

current = -1

while(True):
    try:
        # Keep update switch state
        state = switch.getSwitchState()

        # Camera
        if state == 0:
            program.start(0)

        # Distance
        elif state == 1:
            program.start(1)

        time.sleep(0.2)

    except(KeyboardInterrupt):
        print "Finishing"
        program.stop()
        break

    except:
        print "Unexpected error"
        raise
