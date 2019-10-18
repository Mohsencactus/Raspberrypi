from time import sleep
import cv2 as cv
from imutils.video import VideoStream
#import imutils
webcam = VideoStream(0, True, (480, 368),35).start()
sleep(0.2)

while True:
    frame = webcam.read()
    print(type(frame))
    
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        webcam.stop()
        cv.destroyAllWindows()
        break
