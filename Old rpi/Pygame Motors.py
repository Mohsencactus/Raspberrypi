from time import sleep
import pygame as pg
from MoMotors import *
import RPi.GPIO as GPIO

Pins()

pg.init()
pg.display.set_mode((100,100),0)

speed = 1

while True:
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
                pg.quit()
                break

        elif event.type == pg.QUIT:
            print("Exiting!")
            GPIO.cleanup()
            pg.quit()
            break

        elif event.type == pg.KEYUP:
                Stop()
                print("Stop")

GPIO.cleanup()