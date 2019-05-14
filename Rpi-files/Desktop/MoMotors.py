from gpiozero import PWMOutputDevice

Mr1 = 0 
Mr2 = 0
Ml1 = 0
Ml2 = 0

def Pins(W = 19,X = 26,Y = 6,Z = 13):
    global Mr1
    global Mr2
    global Ml1
    global Ml2
    Mr1 = PWMOutputDevice(W)
    Mr2 = PWMOutputDevice(X)
    Ml1 = PWMOutputDevice(Y)
    Ml2 = PWMOutputDevice(Z)    
def Forward(speed = 1):
    Mr1.value = speed
    Mr2.value = 0
    Ml1.value = speed
    Ml2.value = 0
def Backward(speed = 1):
    Mr1.value = 0
    Mr2.value = speed
    Ml1.value = 0
    Ml2.value = speed
def Forwardleft(speed = 1):
    Mr1.value = speed
    Mr2.value = 0
    Ml1.value = 0
    Ml2.value = 0
def Forwardright(speed = 1):
    Mr1.value = 0
    Mr2.value = 0
    Ml1.value = speed
    Ml2.value = 0
def Backleft(speed = 1):
    Mr1.value = 0
    Mr2.value = speed
    Ml1.value = 0
    Ml2.value = 0
def Backright(speed = 1):
    Mr1.value = 0
    Mr2.value = 0
    Ml1.value = 0
    Ml2.value = speed
def Circleleft(speed = 1):
    Mr1.value = speed
    Mr2.value = 0
    Ml1.value = 0
    Ml2.value = speed
def Circleright(speed = 1):
    Mr1.value = 0
    Mr2.value = speed
    Ml1.value = speed
    Ml2.value = 0
def Stop():
    Mr1.value = 0
    Mr2.value = 0
    Ml1.value = 0
    Ml2.value = 0
