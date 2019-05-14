from time import sleep
import pygame as pg
from MoMotors import *
import RPi.GPIO as GPIO


Pins()

Forward(1)
sleep(2)
Stop()

GPIO.cleanup()  

