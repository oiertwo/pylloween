__author__ = 'oier'


"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import pygame
from random import randint
import os
import threading

def playsound(filepath):

    CHUNK = 1024
    wf = wave.open(filepath, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()




def play_random_back():
    backaudiopath = ""
    list = ['Cat.wav', 'Chains.wav', 'Door.wav', 'frogs.wav' ]
    audio = list[randint(0,len(list))]
    playsound(os.path.join(backaudiopath,audio))

def playrandom_horror():
    horroraudiopath = ""
    list = ['Cat.wav', 'Chains.wav', 'Door.wav', 'frogs.wav' ]
    backaudiopath = ""
    audio = list[randint(0,len(list))]
    playsound(os.path.join(horroraudiopath,audio))

