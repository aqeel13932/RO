from gopigo import *
import RPi.GPIO as GPIO
from time import sleep
from time import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def Read():
        Trig=14
        Echo = 15        
        GPIO.setup(Echo,GPIO.IN)
        GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(Trig,GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(Trig,GPIO.LOW)
        start = time()
        while GPIO.input(Echo)==0:
                start = time()
        while GPIO.input(Echo)==1:
                endtime=time()
        time_passed = endtime-start;
        return time_passed*340/2
def Move(val):
        #val*=10
        #if val>0:
        #        val*=10
        if val>150:
                val = 150

        if val<-150:
                val = -150
        #print val

        if val>0:
                set_speed(int(abs(val)))
                bwd()
               # sleep(0.1)
        elif val<0:
                set_speed(int(abs(val)))
                fwd()
               # sleep(0.1)
                '''
def Move2(val):
        val
        #if val>0:
        #        val*=10
        #if val>150:
        #       val = 150
        if val<-150:
                val = -150

        if val>0:
                set_speed(150)
                bwd()
                #sleep(0.1)
        elif val<0:
                set_speed(150)
                fwd()
                #sleep(0.1)
                '''
def TestReader():
        for i in range(10):
                print Read()
                sleep(1)
        
P=1500
I=10
D=10
en=0
en1=0
en2=0
distance=0.3
Rn1=0
while 1:
        
        val = Read()
        en = distance-val
        Rn =Rn1+P*(en-en1)+(I*(en+en1)/float(2))+D*(en-2*en1+en2)
        print 'Read:{},P:{},I:{},D:{},RN:{}'.format(val,P*(en-en1),(I*(en+en1)/float(2)),D*(en-2*en1+en2),Rn)
        Move(Rn)
        en2=en1
        en1=en
        Rn1=Rn
        
