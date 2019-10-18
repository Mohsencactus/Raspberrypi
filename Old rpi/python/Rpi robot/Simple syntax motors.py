from time import sleep
import pygame as pg
import RPi.GPIO as GPIO
from MoMotors import *

Pins()

Forward(1)
sleep(2)
Stop()

GPIO.cleanup()  

