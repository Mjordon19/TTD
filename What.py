Import RoboPiLib as RPL

Near = RPL.digitalread(23)
motorL = 1
motorR= 0

Robo = 0
while Robo is 0:
  if near is 0:
  RPL.servowrite(motorL, 1000)
  RPL.servowrite(motorR, 2000)
   Print "go"

  if near is 0:
RPL.servowrite (motorL, 0)
RPL.servowrite (motorR, 0)
Print "end"
