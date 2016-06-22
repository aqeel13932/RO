import Adafruit_CharLCD as LCD
import random
import os
import datetime
import time
from time import sleep

#few standard phrases 
PH_START_GAME = "Shake to begin!"
PH_GAME_FINISHED = "Boom! Game over!\n Shake again! :)"


lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,1,1)
lcd.clear()
		

class Display:
	def __init__(self,status):	
		with open('words2.txt') as words:
			self.lst =map(lambda x:x.strip(), words.readlines())
		self.gstatus = status
	def getWord(self):
		return self.lst[random.randint(0,len(self.lst))]
	

	def showWord(self,word):
		lcd.clear()
		lcd.message(word)
	
	def display(self):
                #game not started yet
		if (self.gstatus.status == 0):
                        #print('hello world')
			self.showWord(PH_START_GAME)
			
		#game started
		elif (self.gstatus.status == 1):
                        
                        #new word is requested
                        if (self.gstatus.changeword):
                                self.gstatus.wordupdated()
                                self.showWord('Ready')
                                sleep(0.4)
                                self.showWord('Get Set')
                                sleep(0.4)
                                self.showWord('Go')
                                sleep(0.4)                                
                                word = self.getWord()	 
                                self.showWord(word)
                                self.gstatus.currentword= word.lower()
                                
                #Exploded
		elif (self.gstatus.status == 2):
			self.showWord(PH_GAME_FINISHED)
			
	def button_status(self):
		return lcd.is_pressed(LCD.SELECT)
	def clear(self):
                lcd.clear()

#d = Display()
#d.showWord(PH_GAME_FINISHED)
#d.playGame()

