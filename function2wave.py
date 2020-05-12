import numpy as np
from scipy.io.wavfile import write

samplerate = 44100
f = 220              #Frequenz des Sinus-Tons in Hz
t = 3                #Dauer des Tons in s
p = 50               #Lautstärke von 1 bis 100   

g = np.linspace(0, 1*t, samplerate*t)
data = np.sin(2 * np.pi * f * g)
scaled = np.int16(data/np.max(np.abs(data))*p**2.2)
write("example.wav", samplerate, scaled)