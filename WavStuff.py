import math
import operator
import pyaudio, wave, sys
import struct
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import random, time
from scipy.fftpack import fft
from tkinter import TclError
from pylab import*
from scipy.io import wavfile
import random

class WavStuff:
    @staticmethod
    def getWavFile(filePath):
        samp_rate = 44100
        loaded_wave = wave.open(filePath, 'rb')
        p = pyaudio.PyAudio()
        stream=p.open(format=p.get_format_from_width(loaded_wave.getsampwidth()), channels=loaded_wave.getnchannels(), rate=loaded_wave.getframerate(), input=True, output=True, frames_per_buffer=1024)
        wave_seconds = loaded_wave.getnframes() / samp_rate
        return samp_rate, wave_seconds, loaded_wave, stream
    
    @staticmethod
    def getWavFileByte(filePath):
        CHUNK = 1024*4
        wave_file = wave.open(filePath, 'rb')
        x = []
        count = 0
        while count <= (int(wave_file.getnframes()/CHUNK)):
            data = wave_file.readframes(CHUNK)
            data_int = np.frombuffer(data, dtype=np.int16)
            x.append(data_int)
            count=count+1
        result=[]
        for list in x:
            if(list.any()):
                result.append(min(list))
                result.append(max(list))
        y_max = np.amax(result)
        y_min = np.amin(result)
        return y_max, y_min