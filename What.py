Import setup
Import RoboPiLib as RPL

Near = RPL.digitalread(23)
motorL = 2
motorR= 0

Robo = 0
While Robo is 0:
  If near is 0:
  RPL.servowrite(motorL, 1000)
  RPL.servowrite(motorR, 2000)
   Print "go"

  If near is 0:
RPL.servowrite (motorL, 0)
RPL.servowrite (motorR, 0)
Print "end"
