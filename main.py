__author__ = 'oier'


import record
import playsound
import visualization as vis
from random import randint

def pylloween():
    STREAM_TIME = 0.1
    VAR_VALUE = 150000
    while 1:
        mean, var = record.stream_micro(STREAM_TIME)
        if (var > VAR_VALUE):
            #sound festival:
            if (randint(0,10) > 5):
                playsound.play_random_back()
            else:
                playsound.playrandom_horror()

            if (randint(0,10) > 6):
                vis.lightning()

pylloween()


