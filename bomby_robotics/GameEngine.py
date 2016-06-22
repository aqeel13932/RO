import Adafruit_CharLCD as LCD
import random
import os
import datetime
import time
from Display import Display
from Sound import Sound


#This is status of the game
#0 - initialized
#1 - game is in progress
#2 - word guessed - switch words
#4 - game finished

class Status:
	status = 0
	

class GameEngine:
	display = Display()
	sound = Sound()
	EXTERNAL_STATUS = Status()
	def playGame(self):
		pressed = 0
		self.EXTERNAL_STATUS.status = 0
		self.display.display(self.EXTERNAL_STATUS)
		while(1):
			if(self.display.button_status()):	
				pressed = 1
			if(pressed == 1):
				pressed = 0
				self.EXTERNAL_STATUS.status = 2
				self.display.display(self.EXTERNAL_STATUS)		
				print self.EXTERNAL_STATUS.status
			if(self.EXTERNAL_STATUS.status == 4):
				self.display.display(self.EXTERNAL_STATUS)				



ge = GameEngine()
ge.playGame()








