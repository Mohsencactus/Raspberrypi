print('Hello Mohsen')
import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
for i in range (0,10):
 print(i)
 GPIO.output(8, GPIO.HIGH) 
 sleep(0.5) 
 GPIO.output(8, GPIO.LOW) 
 sleep(0.5) 
