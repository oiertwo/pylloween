__author__ = 'oier'


"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import numpy as np

def stream_micro(time):
    CHUNK = 128
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = time

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("* reading microphone")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        my_data = np.fromstring(data, np.int16)
        mean = np.mean(my_data)
        var = np.var(my_data)

    print("* done geting data")

    stream.stop_stream()
    stream.close()
    p.terminate()
    return(mean, var)