Runing = False
Blende = 0
pressed = False

#Runing or Not Runing
def isRuning():
    return Runing
def setRuning():
    Runing = not Runing

def isPressed():
    return pressed
def setPressed():
    pressed = not pressed

#Blende Funktionen
def getBlende():
    return Blende
def setBlende(i):
    Blende = i
