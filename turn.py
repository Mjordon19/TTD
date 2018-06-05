import RoboPiLib as RPL
import setup import RPL 
RPL.RoboPiInit("/dev/ttyAMOA0",115200)

import sys, tty, termios, signal
#gets the motors going

motorL = 0
motorR = 2
sensor_pin = 18
nearby = RPL.digitalread(23)

robot = 0

while robot is 0:
    if nearby is 0:
        RPL.servowrite(motorL, 1000)
        RPL.servowrite(motorR, 2000)
        print "start"
    if nearby is 1:
        RPL.servowrite(motorL, 0)
        RPL.servowrite(motorR, 0)
        print "stop"
