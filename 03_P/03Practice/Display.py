import os
import datetime
import Adafruit_CharLCD as LCD
def getCPUtemperature():
    res=os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=","").replace("'C\n",""))

def getTimeText():
    t = datetime.datetime.now()
    return '{}:{}:{}'.format(t.hour,t.minute,t.second)
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,1,1)
while 1:
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        lcd.message('{}\n{}'.format(getCPUtemperature(),getTimeText()))
    if (lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        break

