from Arduino import Arduino
from time import sleep

arduino = Arduino()
arduino.pinMode(13, "OUTPUT")
while True:
    arduino.digitalWrite(13, "HIGH")
    sleep(1)
    arduino.digitalWrite(13, "LOW")
    sleep(1)
