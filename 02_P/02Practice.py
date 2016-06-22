from gopigo import *
from time import sleep
speed = 100
#CALCULAE DURATION
def calculateduration(length):
    global speed
    duration = float(length)/float(speed)
    duration *=10
    return duration
def rotationduration(angle):
    global speed
    av = speed/6.5
    print 'av',av
    duration = (1.5/av)*5.4
    return duration
def Task1():
    fwd()
    sleep(1)
    bwd()
    sleep(1)
    stop()

def Movefwd(duration):
    #duration = calculateduration(length)
    fwd()
    sleep(duration)
    stop()
def Movebwd(duration):
    #duration = calculateduration(length)
    bwd()
    sleep(duration)
    stop()

def Moveright(duration):
    
    right_rot()
    sleep(duration)
    stop()
def Task2(length):
    
    rotateduration = 0.60
    duration = calculateduration(length)
    Movefwd(duration)
    Moveright(rotateduration)
    Movefwd(duration)
    Moveright(rotateduration)
    Movefwd(duration)
    Moveright(rotateduration)
    Movefwd(duration)
    Moveright(rotateduration)
def Task3():
    #Long path
    Movebwd(4.1)
    Moveright(0.65)
    
    Movebwd(2.7)
    Moveright(1)
    Movebwd(2)
set_speed(100)
#Task1()
#Task2(10)
Task3()
print 'hello'
