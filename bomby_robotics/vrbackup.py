#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import pyaudio
import wave
import speech_recognition as sr
from time import time,sleep

def ReadAndInterpret():
    # obtain audio from the microphone
    r = sr.Recognizer()
    t = time()
    with sr.Microphone() as source:
        print("Say something!")
        audio1 = r.record(source,2)
    print('second sentence')
    with sr.Microphone() as source:
        print("Say something!")
        audio2 = r.record(source,2)
        
    with open('audio1.flac','wb') as f:
        f.write(audio1.get_flac_data())
    with open('audio2.flac','wb') as f:
        f.write(audio2.get_flac_data())
    audio = sr.AudioData(audio1.frame_data+audio2.frame_data,audio1.sample_rate,audio1.sample_width)
    with open('audio.flac','wb') as f:
        f.write(audio.get_flac_data())

    #return

    print time()-t
    print ("Stopped Listning")
    print (audio.sample_width,len(audio.frame_data),audio.sample_rate)

    '''
    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    '''
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # recognize speech using Wit.ai
    WIT_AI_KEY ="RHGDIA7UYYCVUILELWSVOEJAR2C64JJE"# "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

#ReadAndInterpret()
#t1 = Thread(target = ReadAndInterpret)
#t2 = Thread(target = ReadAndInterpret)
#t1.start()
#t2.start()
