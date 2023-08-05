import numpy  as  np
import  matplotlib.pyplot as  plt
from scipy.signal import spectrogram


def plot_signal(time, Signal):
    plt.figure(figsize=(12,6))
    plt.plot(time, Signal)
    plt.title("periodic sinwave 440 HZ")
    plt.xlabel("time")
    plt.ylabel("Amplitude")
    plt.xlim(0, 0.01) # lmit the x axes to have a clear plot
    plt.show()

def plot_periodogram(frequencies, values):
    plt.figure(figsize=(12,6))
    plt.plot(frequencies, 10*np.log10(values))
    plt.title('Periodogram of the First Segment')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density (dB)')
    plt.show()


def plot_PSD(frequencies , psd):
    plt.figure(figsize=(12, 4))
    plt.plot(frequencies, 10 * np.log10(psd))
    plt.title('Power Spectral Density (PSD)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density (dB)')
    plt.show() 


# variables
fs  = 8000 # sampling frequancy 
f = 440 # signal frequancy
duration = 1 # second

# signal
t  = np.arange(int(fs*duration))/fs # devid  by fs  to make sure samples are 1/fs apart from each other
signal = np.sin(2 * np.pi * f * t )
plot_signal(t,signal)

# periodogram 
# variables
npersegm = 1024
noverlap = npersegm // 2 
Segments = [signal[i:i+npersegm] for i in range(0,len(signal),npersegm-noverlap)]

# the last two segmenst have diffrent lenghts and will cause  a problem when we try to apply windowing
for  seg,i  in zip(Segments,range(len(Segments))): 
    if len(seg) != npersegm:
        Segments[i] = np.pad(seg,(0,npersegm-len(seg)))
        # print(len(seg))
        # print(len(Segments[i]))

# windowing each Segment  --> use  the Hanning window

window = np.hanning( npersegm)
windowed_segments = [window * seg for seg  in Segments]

#Frequancy bins 
F_bins = [np.fft.rfft(seg) for seg  in windowed_segments] # ----> we use the rfft to discart the negative part of the  FT becaus the x signal is a real one

# periodogram  
periodogram = [np.abs(seg)**2 for seg in F_bins]
frequencies = np.fft.rfftfreq(npersegm, 1/fs)
plot_periodogram(frequencies,periodogram[0])

#PSD Power Spectral Density (dB)
PSD = np.mean(periodogram,axis=0,)
plot_PSD(frequencies,PSD)


# 


# Compute the spectrogram
frequencies, times, Sxx = spectrogram(signal, fs, window='hann', nperseg=npersegm, noverlap=noverlap)

# Plot the spectrogram
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='auto', cmap='inferno')
plt.title('Spectrogram')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Intensity [dB]')
plt.show()




