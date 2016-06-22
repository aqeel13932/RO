from gopigo import *
import RPi.GPIO as GPIO
from time import sleep
from time import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def blinkfor5seconds():
        for i in range(5):
                led_on(0)
                led_on(1)
                sleep(0.5)
                led_off(0)
                led_off(1)
                sleep(0.5)
def Task1():
        GPIO.setup(14,GPIO.IN)
        while True:
                Digital_in = GPIO.input(14)
                print Digital_in
                if Digital_in>0:
                        blinkfor5seconds()
                sleep(0.1)

def Task2():
        while True:
                reading=analogRead(1)
                if reading>800:
                        print 'Extreem light source,',reading
                elif reading<100:
                        print 'Turn on the light ',reading
                else:
                        print 'nice light :) ',reading
                sleep(0.5)
def FirstSensor():
        GPIO.setup(9,GPIO.IN)
        GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(11,GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(11,GPIO.LOW)
        while GPIO.input(9)==0:
                start = time()
        while GPIO.input(9)==1:
                endtime=time()
        time_passed = endtime-start;
        print time_passed,'range1:',time_passed*340/2
def SecondSensor():
        GPIO.setup(15,GPIO.IN)
        GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(14,GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(14,GPIO.LOW)
        while GPIO.input(15)==0:
                start = time()
        while GPIO.input(15)==1:
                endtime=time()
        time_passed = endtime-start;
        print time_passed,'range2:',time_passed*340/2
def Task3():
        FirstSensor()
        #SecondSensor()
try:
        #Task1()
        #Task2()
        Task3()
except KeyboardInterrupt:
        GPIO.cleanup()
