#!/usr/bin/env python
#coding: utf8

import speech_recognition as sr  
import os
   
# obtain audio from the microphone  
r = sr.Recognizer()  

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
            response = "OK!"
        os.system("espeak -ven+f3 -k5 -s150 {0}".format(response))

    except sr.UnknownValueError:  
        print("Sphinx could not understand audio")  
    except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))  
