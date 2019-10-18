import RPi.GPIO as rp
from time import sleep

servo1 = 20

rp.setmode(rp.BCM)
rp.setwarnings(False)

rp.setup(servo1,rp.OUT)
pwm1 = rp.PWM(servo1,50)
pwm1.start(6)
duty = 6
while True:
  pwm1.ChangeDutyCycle(duty)
  print(duty)
  duty = duty + 0.1
  if duty >= 11:
    duty = 2
  sleep(1)

pwm1.stop() 
rp.cleanup()
