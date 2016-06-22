from gopigo import *
import RPi.GPIO as GPIO
from time import sleep,time
# pin numbers are defined here, yours may be different
#PWM = 10
#DIR1 = 9
#DIR2 = 11

#[PWD,DIR1,DIR2]
#LeftMotor = [10,11,9]
#RightMotor =[22,27,17]
# reference pins by GPIO numbers
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)

# set pins as outputs
#GPIO.setup(LeftMotor,GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(RightMotor,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15,GPIO.OUT,initial=GPIO.LOW)
# give power to motor
#set_speed(255)
#motor_bwd()
def MoveForward(duration ,speed):
        GPIO.output(LeftMotor[1],GPIO.HIGH)
        GPIO.output(RightMotor[1],GPIO.HIGH)
        speed = speed /10
        runtime = 0.001 * speed
        stoptime = 0.01-runtime
        duration = duration *100
        print runtime , stoptime,duration
        for i in range(duration):
                GPIO.output(LeftMotor[0],GPIO.HIGH)
                GPIO.output(RightMotor[0],GPIO.HIGH)
                sleep(runtime)
                GPIO.output(LeftMotor[0],GPIO.LOW)
                GPIO.output(RightMotor[0],GPIO.LOW)
                sleep(stoptime)
def Forward(duration,speed):
        GPIO.output(LeftMotor[1],GPIO.HIGH)
        GPIO.output(RightMotor[1],GPIO.HIGH)
        p1 = GPIO.PWM(LeftMotor[0],100)
        p2 = GPIO.PWM(RightMotor[0],100)
        p1.start(speed)
        p2.start(speed)
        sleep(duration)
        p1.stop()
        p2.stop()
        GPIO.output(LeftMotor[1],GPIO.LOW)
        GPIO.output(RightMotor[1],GPIO.LOW)
        
def Backward(duration,speed):
        GPIO.output(LeftMotor[2],GPIO.HIGH)
        GPIO.output(RightMotor[2],GPIO.HIGH)
        p1 = GPIO.PWM(LeftMotor[0],100)
        p2 = GPIO.PWM(RightMotor[0],100)
        p1.start(speed)
        p2.start(speed)
        sleep(duration)
        p1.stop()
        p2.stop()
        GPIO.output(LeftMotor[2],GPIO.LOW)
        GPIO.output(RightMotor[2],GPIO.LOW)     
def Right(duration,speed):
        GPIO.output(LeftMotor[1],GPIO.HIGH)
        GPIO.output(RightMotor[2],GPIO.HIGH)
        p1 = GPIO.PWM(LeftMotor[0],100)
        p2 = GPIO.PWM(RightMotor[0],100)
        p1.start(speed)
        p2.start(speed)
        sleep(duration)
        p1.stop()
        p2.stop()
        GPIO.output(LeftMotor[1],GPIO.LOW)
        GPIO.output(RightMotor[2],GPIO.LOW) 
def Left (duration,speed):
        GPIO.output(LeftMotor[2],GPIO.HIGH)
        GPIO.output(RightMotor[1],GPIO.HIGH)
        p1 = GPIO.PWM(LeftMotor[0],100)
        p2 = GPIO.PWM(RightMotor[0],100)
        p1.start(speed)
        p2.start(speed)
        sleep(duration)
        p1.stop()
        p2.stop()
        GPIO.output(LeftMotor[2],GPIO.LOW)
        GPIO.output(RightMotor[1],GPIO.LOW)
        #Clockwise = True, AntiClockWise = False;
def ServoTest (duration,speed,direction=True):
        realspeed =1.5+0.2*speed if direction else (1.5-0.2*speed)
        realspeed= (realspeed/20)*100
        print realspeed , 0.2*speed
        p1.ChangeDutyCycle(realspeed)
        #print realspeed
        sleep(duration)
        #GPIO.cleanup()
#Duration in Seconds,speed 0->1 , direction True clockwise , false anticlockwise
def ServoTest2 (duration,speed,direction=True):
    speed *=0.2
    midlepiont=1.43
    upduration =(midlepiont+speed) if direction else (midlepiont-speed)
    print upduration
    upduration *=0.001
    print upduration
    start = time()
    GPIO.output(15,GPIO.LOW)
    while (time()-start)<duration:
        GPIO.output(15,GPIO.HIGH)
        sleep(upduration)
        GPIO.output(15,GPIO.LOW)
        sleep(0.02-upduration)
        
# Enter your code here
#Set Direction 1 High
print "Direction 1 High"

#Set Power to High
#MoveForward(1,10)
#Forward(2,90)
#Left(1,90)
#Right(1,90)
#Backward(2,90)
#Left(1,90)
#Right(1,90)
#Backward(2,90)
#ServoTest(2,19)
#sleep(0.5)
#ServoTest(2,15)
#sleep(0.5)
#ServoTest(2,8)
#sleep(0.5)
#COUNTER
#ServoTest2(2,0,True)
p1 = GPIO.PWM(15,50)
p1.start(0)
p1.ChangeDutyCycle(6.2)
sleep(5)
p1.ChangeDutyCycle(6.7)
sleep(5)
p1.ChangeDutyCycle(8.2)
sleep(5)
p1.ChangeDutyCycle(7.7)
sleep(5)
#p1.ChangeDutyCycle(7.5)
#sleep(5)
#ServoTest(2,1,True)
#ServoTest(2,0,True)
#CLOCKWISE
#ServoTest(2,1,False)
#ServoTest(2,0.5,False)

GPIO.output(15,GPIO.LOW)
p1.stop()
#Set Direction 1 Low
#GPIO.output(LeftMotor[1],GPIO.LOW)
#GPIO.output(RightMotor[1],GPIO.LOW)
#Set Power to Low
#GPIO.output(LeftMotor[0],GPIO.LOW)
#GPIO.output(RightMotor[0],GPIO.LOW)
stop()
