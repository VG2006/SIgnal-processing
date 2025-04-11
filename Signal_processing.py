import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks



sample_rate, data = wavfile.read('signal_modulated_noisy_audio.wav')
print(f"Sample rate: {sample_rate} Hz")
print(f"Data shape: {data.shape}")

if len(data.shape) == 2:
    data = data.mean(axis=1)  

duration = len(data) / sample_rate
time = np.linspace(0., duration, len(data))

plt.figure(figsize=(10, 4))
plt.plot(time[:5000], data[:5000])  
plt.title("Modulated Signal (Time Domain)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

from scipy.fft import fft, fftfreq

n = len(data)
yf = fft(data)
xf = fftfreq(n, 1 / sample_rate)
magnitude = np.abs(yf[:n//2])

plt.figure(figsize=(10, 4))
plt.plot(xf[:n//2], np.abs(yf[:n//2]))  
plt.title("FFT of Modulated Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid()
plt.show()


import numpy as np
t = np.arange(len(data)) / sample_rate

max_index = np.argmax(magnitude)
Fc = xf[max_index]
demodulated = data * np.cos(2 * np.pi * Fc * t)


plt.figure(figsize=(10, 4))
plt.plot(t[:5000], demodulated[:5000])
plt.title("Demodulated Signal (Before Filtering)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

from scipy.signal import butter, filtfilt

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs 
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs=44100, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return filtfilt(b, a, data)

filtered_signal = lowpass_filter(demodulated, cutoff=Fc, fs=sample_rate)

plt.figure(figsize=(10, 4))
plt.plot(t[:5000], filtered_signal[:5000])
plt.title("Filtered (Recovered) Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


from scipy.io.wavfile import write

filtered_signal = filtered_signal / np.max(np.abs(filtered_signal))

write("Recovered.wav", sample_rate, (filtered_signal * 32767).astype(np.int16))


import os 
print("Saved at:", os.path.abspath("Recovered.wav"))


