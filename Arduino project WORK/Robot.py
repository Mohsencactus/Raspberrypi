from Arduino import Arduino
from time import sleep

arduino = Arduino()

class Motors:
    def __init__(self,pins=[2,4,7,8],servo = 9):
        self.m1 = pins[0]
        self.m2 = pins[1]
        self.m3 = pins[2]
        self.m4 = pins[3]
        self.servo = servo
        self.deg = 90
        self.status = "Started"
        self.time = 50
        arduino.pinMode(self.m1, "OUTPUT")
        arduino.pinMode(self.m2, "OUTPUT")
        arduino.pinMode(self.m3, "OUTPUT")
        arduino.pinMode(self.m4, "OUTPUT")
        arduino.Servos.attach(self.servo)
        arduino.Servos.write(self.servo,self.deg)

    def delay(self,millis):
        sleep(millis/1000)
    def Changedelaytime(self,time):
        self.time = time

    def Stop(self,delay='None'):
        self.status = "Stoped"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "LOW")
    def Forward(self,delay='None'):
        self.status = "Going Forward"
        arduino.digitalWrite(self.m1, "HIGH")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "HIGH")
        arduino.digitalWrite(self.m4, "LOW")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Backward(self,delay='None'):
        self.status = "Going Backward"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "HIGH")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "HIGH")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Turnleft(self,delay='None'):
        self.status = "Turning Right"
        arduino.digitalWrite(self.m1, "HIGH")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "HIGH")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Turnright(self,delay='None'):
        self.status = "Turning Left"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "HIGH")
        arduino.digitalWrite(self.m3, "HIGH")
        arduino.digitalWrite(self.m4, "LOW")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Rightmotorforward(self,delay='None'):
        self.status = "Right Motor Going Forward"
        arduino.digitalWrite(self.m1, "HIGH")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "LOW")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Rightmotorbackward(self,delay='None'):
        self.status = "Right Motor Going Backorward"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "HIGH")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "LOW")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Leftmotorforward(self,delay='None'):
        self.status = "Left Motor Going Forward"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "HIGH")
        arduino.digitalWrite(self.m4, "LOW")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Leftmotorbackward(self,delay='None'):
        self.status = "Left Motor Going Backward"
        arduino.digitalWrite(self.m1, "LOW")
        arduino.digitalWrite(self.m2, "LOW")
        arduino.digitalWrite(self.m3, "LOW")
        arduino.digitalWrite(self.m4, "HIGH")
        if delay == "None":
            millis = self.time
        else :
            millis = delay
        sleep(millis/1000)
    def Servoplus(self,degree=1):
        self.status = "Adding to Servo Position"
        if self.deg < 180 and (self.deg+degree) < 180 and (self.deg+degree) > 0:
            self.deg = self.deg + degree
        elif (self.deg+degree) > 180 :
            self.deg = 180
        elif (self.deg+degree) < 0:
            self.deg = 0
        arduino.Servos.write(self.servo,self.deg)
    def Servopos(self,degree):
        self.status = "Servo Moving To Position"
        self.deg = degree
        arduino.Servos.write(self.servo,self.deg)
