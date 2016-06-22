#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import pyaudio
import wave
import speech_recognition as sr
from time import time,sleep
from threading import Thread
from Queue import Queue
import copy
class AudioListener():
    def __init__(self,status):
        self.r = sr.Recognizer()
        self.gstatus = status
        self.que = Queue()
    def listen(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.record(source,2)
        return audio
    def AudioListenerOperator(self):
        print 'Listener Started'
        #initialize the first entry
        a1=sr.AudioData('',1,1)
        while self.gstatus.status!=3:
            #never start recording before the game begin
            if self.gstatus.status!=1:
                sleep(0.5)
                continue
            a2 = self.listen()
            audio = sr.AudioData(a1.frame_data+a2.frame_data,a2.sample_rate,a2.sample_width)
            self.que.put(a2)
            self.que.put(audio)
            a1 = a2
        print 'Listener Thread Ended\n'
    #get words from the audio
    def AudioInterpreter(self):
        while 1:#self.gstatus==1:
            if self.gstatus.status==3:
                break
            if self.que.empty():
                print '=================EMPTY======================'
                sleep(0.5)
                continue
            try:
                
                #In case game exploded or closing 
                if self.gstatus.status!=1:
                    self.que.queue.clear()
                    continue
                print '==================Getting Text================'
                audio = self.que.get()
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                gwords = self.r.recognize_google(audio)
                print '====GOOGLE:{}==='.format(gwords)
                if self.gstatus.currentword in gwords.lower().split(' '):
                    print '=================VICTORY==============='
                    self.gstatus.changeword=True
                    self.que.queue.clear()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            # recognize speech using Wit.ai
            WIT_AI_KEY ="RHGDIA7UYYCVUILELWSVOEJAR2C64JJE"# "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
            try:
                witwords = self.r.recognize_wit(audio, key=WIT_AI_KEY)
                print '====WIT:{}==='.format(witwords)
                if self.gstatus.currentword in witwords.lower().split(' '):
                    print '=================VICTORY==============='
                    self.gstatus.changeword=True
                    self.que.queue.clear()                
                print("Wit.ai thinks you said " + witwords)
            except sr.UnknownValueError:
                print("Wit.ai could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Wit.ai service; {0}".format(e))
        print 'Interpreter Thread Ended\n'
        


