import pygame as pg
import cv2 as cv
import numpy as np

class framer():
    def __init__(self,camera=0):
        self.webcam = cv.VideoCapture(camera)
        pg.init()
        self.window = pg.display.set_mode([640,480])
    def frameread(self):
        self.frame = self.webcam.read()[1]
        return self.frame
    def imshow(self,frame):
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        self.window.blit(frame, (0,0))
        pg.display.update()
    def imshowrgb(self,frame):
        frame = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pg.surfarray.make_surface(frame)
        self.window.blit(frame, (0,0))
        pg.display.update()
