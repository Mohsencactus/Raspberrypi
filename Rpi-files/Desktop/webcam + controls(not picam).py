from time import sleep
import pygame as pg
from MoMotors import *
import RPi.GPIO as GPIO
import cv2 as cv
import numpy as np

Pins()

pg.init()
window = pg.display.set_mode([640,480])

speed = 1

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.flip(frame,2)
    frame = np.rot90(frame)
    frame = pg.surfarray.make_surface(frame)
    frame = pg.transform.scale(frame,(640,480))
    
    window.blit(frame, (0,0))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_x:
                print("Coming soon")

            elif event.key == pg.K_w:
                print("Going Forward")
                Forward(speed)

            elif event.key == pg.K_s:
                print("Going Backward")
                Backward(speed)

            elif event.key == pg.K_a:
                print("Going Forward-left")
                Forwardleft(speed)

            elif event.key == pg.K_z:
                print("Going Backward-left")
                Backleft(speed)

            elif event.key == pg.K_d:
                print("Going Forward-right")
                Forwardright(speed)

            elif event.key == pg.K_c:
                print("Going Backward-right")
                Backright(speed)

            elif event.key == pg.K_e:
                print("Doing a Circle-right")
                Circleright(speed)

            elif event.key == pg.K_q:
                print("Doing a Circle-left")
                Circleleft(speed)

            elif event.key == pg.K_l:
                print("Exiting!")
                GPIO.cleanup()
                cv.destroyAllWindows()
                pg.quit()

        elif event.type == pg.QUIT:
            print("Exiting!")
            GPIO.cleanup()
            cv.destroyAllWindows()
            pg.quit()
            break

        elif event.type == pg.KEYUP:
                Stop()
                print("Stop")
