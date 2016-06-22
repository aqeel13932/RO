import serial 
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
ser.write(b'YO Yo yo')
ser.close()
import hashlib

myId = 2
generalId = 0

separator = '+'

while 1: 
	with serial.Serial('/dev/ttyACM0', 19200, timeout = 1) as ser:
		x = ser.readline()
		if len(x.split(separator))>=5:
			xSplit = x[x.find('s'+ separator):x.find(separator+'e')+2].split(separator)

		else:
			continue


		
#		print "aaaa    " + ''.join(xSplit)
#		print len(xSplit)
#		print x
		if ( int(xSplit[1]) == myId or int(xSplit[1]) == generalId):
			text = hashlib.md5()
			text.update(xSplit[2])
			#print xSplit[2]
			if (text.digest() == xSplit[3]):
				print xSplit[2]
#		
#				
#
#		if ((x[0] == 's' and s[-1] == 'e') == False):
#			ser.flush()
#			continue
#		else: 
#		print(x)
