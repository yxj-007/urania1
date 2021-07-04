import os
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from thinkdsp import decorate
from matplotlib import pyplot
from thinkdsp import read_wave

wave = read_wave('F:\signal\mall.wav')
wave.make_audio()
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
pyplot.show()