from picamera import PiCamera
from time import sleep
from picamera.array import PiRGBArray
import cv2

# Set up PiCamera and let it warm up
camera = PiCamera()
raw = PiRGBArray(camera)
sleep(0.1)


# Capture to a PiRGBArray
camera.capture(raw, format="bgr")
image = raw.array

# Use OpenCV's gui to show the image
cv2.imshow("Preview", image)
cv2.waitKey(0) # Wait for key press to close preview
