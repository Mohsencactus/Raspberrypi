import pygame as pg
import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

pg.init()
window = pg.display.set_mode([640,480])

while True:
    _,frame = webcam.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pg.surfarray.make_surface(frame)
    window.blit(frame, (0,0))
    pg.display.update()
