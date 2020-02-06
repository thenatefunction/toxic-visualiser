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

class ToxicVisualiser:
    @staticmethod
    def toxicVisualiser(samp_rate, y_max, y_min, loaded_wave, stream):
        CHUNK = 1024*4
        mpl.style.use('seaborn')
        sns.set_style("dark")
        sns.set_context("poster")
        fig, (ax, ax2) = plt.subplots(2)
        x=np.arange(0, 16*CHUNK, 8) #step size 2
        x_fft = np.linspace(0, samp_rate, CHUNK)
        
        line, = ax.plot(x, (np.random.rand(2*CHUNK)), '-', lw=1)
        line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK), '-', lw=1)
        
        ax.set_ylim(y_max, y_min)
        ax.set_xlim(0, CHUNK/2)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.yaxis.set_ticklabels([])
        ax.patch.set_facecolor('black')
        ax.patch.set_alpha(.5) #transparency
        ax2.set_xlim(20,samp_rate/2)
        ax2.get_xaxis().set_visible(False)
        ax2.yaxis.set_ticklabels([])
        ax2.patch.set_facecolor('black')
        ax2.patch.set_alpha(.5) #transparency
        line.set_color("black")
        line_fft.set_color("black")
        
        colors = ["#000000", "#051802", "#0f4706", "#155e08", "#1a760a", 
               "#1f8e0b", "#24a50d", "#29bd0f"]
        frame_count=0
        start_time=time.time()
        
        plt.ion()
        while True:
            plt.show()
            data = loaded_wave.readframes(CHUNK)
            data_int = np.fromstring(data, dtype=np.int16)
            
            line.set_ydata(data_int)
            
            y_fft = fft(data_int)
            line_fft.set_ydata(np.abs(y_fft[0:CHUNK])*2 / (10000 * CHUNK))
            try:
                fig.canvas.draw()
                fig.canvas.flush_events()
                #write to stream to play sound                    
                stream.write(data)
                frame_count = frame_count + 1
                
                #random background color
                ax.patch.set_facecolor(random.choice(colors))
                ax2.patch.set_facecolor(random.choice(colors))
                
            except TclError:
                frame_rate = frame_count/(time.time() - start_time)
                print("stream stopped")
                print('average frame rate = {:.0f} FPS'.format(frame_rate))
                break