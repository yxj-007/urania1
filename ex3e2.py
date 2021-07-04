import os
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from thinkdsp import decorate
from matplotlib import pyplot
from thinkdsp import read_wave


PI2 = 2 * np.pi

class SawtoothChirp(Chirp):
    def evaluate(self, ts):
        
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

signal = SawtoothChirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=4000)
wave.apodize()
wave.make_audio()
sp = wave.make_spectrogram(256)
sp.plot()
plt.xlabel('Time(s)')
pyplot.ylabel('Freq(hz)')
pyplot.show()