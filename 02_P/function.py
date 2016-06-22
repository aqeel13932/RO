#from gopigo.gopigo import *
from time import sleep

#Calculate duration depending on speed & length
def calculateduration (length):
    global speed
    duration = float(length)/float(speed)
    #optimality achiever
    alpha = float(0)
    duration = duration+alpha*duration
    return duration

#Caculate the speed based on precentage
def setspeedprecentage(percentspeed):
    if percentspeed>1 :
        return
    global speed
    speed = percentspeed*255
    set_speed(speed)

#Move robot 1 sec to front , 1 sec to back
def Task1():
    fwd()
    sleep(1)
    bwd()
    sleep(1)
    stop()

#Move forward for specific length
def Movefwd(length):
    duration = calculateduration(length)
    fwd()
    sleep(duration)
    stop()

def Moveright(duration):
    right()
    sleep(duration)
    stop()
#Move in seqare of were you choose the length
def Task2(length):
    duration = calculateduration(length)
    # How many times to drive in squares
    for i in range(2):
        #First side
        Movefwd(length)
        Moveright(duration)
        #Second Side
        Movefwd(leng)
        Moveright(duration)
        #Third Side
        Movefwd(length)
        Moveright(duration)
        #Fourth Side
        Movefwd(length)
        #Reach Start Point


#Move on shape on the floor as fast as possible
def Task3(length):
    duration = calculateduration(length)

    #Long side
    fwd()
    sleep(duration)
    right()
    sleep(duration)
    fwd()
    sleep(duration)
    right()
    sleep(duration)
    fwd()
    sleep(duration)
    right()
    sleep(duration)
    fwd()
    sleep(duration)
    stop()



try:
    speed = 0
    setspeedprecentage(0.6)
except KeyboardInterrupt:
    stop()