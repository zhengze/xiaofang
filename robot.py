#!/usr/bin/env python
#coding: utf8

import pyttsx
import speech_recognition as sr  
import os
   
# obtain audio from the microphone  
r = sr.Recognizer()  
engine = pyttsx.init()

while True:
    with sr.Microphone() as source:  
        print("Say something!")  
        audio = r.listen(source)  
           
    # recognize speech using Sphinx  
    try:  
        sphinx_text = r.recognize_sphinx(audio) 
        print("Sphinx thinks you said '" + sphinx_text + "'")  
        if sphinx_text == "hi":
            response = "How do you do"
        else:
            response = "Yes"
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:  
        print("Sphinx could not understand audio")  
    except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))  
