from threading import Thread
from Display import Display
from time import sleep
from Sound import Sound
#from vr import AudioListener
from vr_threads_recognition import AudioListener
class Status(object):
    def __init__(self):
        #0- not started
        #1- started
        #2- Exploded
        #3- Closing
        self.status=0
        #True : change the word
        #False: keep the word
        self.changeword=False
        
        #Count how many words been shown
        self.wordscounter=0
        self.currentword=''
    def reset(self):
        self.status=0
        self.changeword=False
        self.wordscounter=0
        self.currentword=''
    def wordupdated(self):
        self.changeword=False
        self.wordscounter+=1
        
    def getstatus(self):
        return self.status
    
#initalize main classes and game status
status = Status()
print status.getstatus()
disp = Display(status)
sound = Sound(status)
alistner = AudioListener(status)
def Displayfunction():
    while status.status!=3:
        disp.display()
        sleep(0.5)
    disp.clear()
    print 'Display Thread Ended \n'

displaythread = Thread(target=Displayfunction)
soundthread= Thread(target=sound.SoundOperator)
listnerthread= Thread(target=alistner.AudioListenerOperator)
#interpterthread= Thread(target=alistner.AudioInterpreter)
def initialize():
    displaythread.start()
    soundthread.start()
    listnerthread.start()
    #interpterthread.start()
    sleep(2)#Replace with Shaking
    status.status=1
    status.changeword=True
    print '2'
    #sleep(50)
    #status.status=2
    #sleep(2)
    #status.status=3
    #disp.clear()

def FinalInitialization():
    displaythread.start()
    soundthread.start()
    listnerthread.start()
    interpterthread.start()
    #Put with Shaking
    status.status=1
    status.changeword=True
    while 1:
        #Game Exploded
        if status.status==2:
            #Put Shaking Here
            status.reset()
            status.status=1
            status.changeword=True
        #Every Second Will Check The game status
        sleep(1)
try:
    initialize()
except:
    status.status=3
