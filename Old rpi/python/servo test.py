import RPi.GPIO as rp
from time import sleep

servo1 = 12
rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setup(servo1,rp.OUT)
pwm1 = rp.PWM(servo1,50)

while True: 
  for i in range(2,12):
    pwm1.ChangeDutyCycle(i)

