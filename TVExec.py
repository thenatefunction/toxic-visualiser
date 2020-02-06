import math
import operator
import pyaudio, wave, sys
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import random, time
from scipy.fftpack import fft
from tkinter import TclError
from WavStuff import WavStuff
from ToxicVisualiser import ToxicVisualiser
from pylab import*
from scipy.io import wavfile
import random

samp_rate, wave_seconds, loaded_wave, stream = WavStuff.getWavFile('file_example_WAV_10MG.wav')
y_max, y_min = WavStuff.getWavFileByte('file_example_WAV_10MG.wav')
ToxicVisualiser.toxicVisualiser(samp_rate, y_max, y_min, loaded_wave, stream)