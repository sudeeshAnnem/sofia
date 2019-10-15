import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
import playsound
from gtts import gTTS
import wolframalpha
from selenium import webdriver
from time import strftime

greetings=['hello sofia','hi','hi sofia','sofia','hey sofia','hey','hello']
num = 1
def sofiaResponse1(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("Sofia: ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 


def sofiaResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        sofiaResponse1('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        #sofiaResponse1('sorry cant hear your voice say it loudly')
        command = myCommand();
    return command
def assistant(command):
    "if statements for executing commands"
    
    if command in greetings :
        script=open("assistant.py", 'r').read()
        exec(script) 
    
             

while True:
    assistant(myCommand())
