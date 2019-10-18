from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2 as cv 
import numpy as np

webcam = PiCamera() #seting the camera

raw = PiRGBArray(webcam)



raw = PiRGBArray(webcam)

while True:
    
    webcam.capture(raw, format="bgr")
    image = raw.array

    cv.imshow('frame',image)
    a = cv.waitKey(1)
###############################################   
    if(ord("q") == a):
        break
cv.destroyAllWindows()
###############################################
