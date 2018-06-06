import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 16
RPL.pinmode(sensor_pin, RPL.INPUT)

while true:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    PTW.post()

    if RPL.digitalread(sensor_pin == 1:
        import RoboPiLib as RPL
        import setup
        RPL.servowrite(0,1000)
        RPL.servowrite(1,2000)
    if RPL.digitalread(sensor_pin) == 0
        import RoboPiLib as RPL
        import setup
        RPL.servowrite(0,1)
        RPL.servowrite(0,0)
