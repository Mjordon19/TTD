
import setup
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 17

RPL.servowrite(motorR, 2000)
RPL.servowrite(motorL, 1000)
RPL.pinmode(sensor_pin, RPL.INPUT)

while RPL.digitalRead(sensor_pin) == 1:
    RPL.servowrite(motorR,2000)
    RPL.servowrite(motorL,1000)
else:
    RPL.servowrite(motorR, 0)
    RPL.servowrite(motorL)
     
