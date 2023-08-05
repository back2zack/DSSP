# Welch's Method for Spectrogram, Periodogram, and Power Spectral Density (PSD) Calculation

This Python script demonstrates how to compute and plot the spectrogram, periodogram, and Power Spectral Density (PSD) of a signal using Welch's method. The signal used in this script is a 440 Hz sine wave, which is a periodic signal.

## Signal Generation

The script first generates a 440 Hz sine wave with a sampling frequency of 8000 Hz and a duration of 1 second. The time array `t` is created such that the samples are 1/fs apart from each other. The sine wave `signal` is then generated using the formula `np.sin(2 * np.pi * f * t)`.

## Periodogram Calculation

The script then calculates the periodogram of the signal. The signal is divided into overlapping segments of length `npersegm` with `noverlap` points of overlap between consecutive segments. The last segment, which may be shorter than `npersegm`, is padded with zeros to make it the same length as the other segments.

A Hanning window of length `npersegm` is applied to each segment. The Fourier Transform of each windowed segment is computed using `np.fft.rfft()`, which computes the Fourier Transform for real-valued inputs and discards the negative frequencies. The periodogram of each segment is then computed as the square of the absolute value of the Fourier Transform.

## Power Spectral Density (PSD) Calculation

The Power Spectral Density (PSD) is calculated as the mean of the periodograms of all segments. This is done using `np.mean(periodogram, axis=0)`. The PSD provides a smoothed estimate of the power at each frequency, averaged over all segments of the signal.

## Spectrogram Calculation

The spectrogram of the signal is computed using `scipy.signal.spectrogram()`, which returns the frequencies, times, and spectrogram of the signal. The spectrogram is a 2D array that shows the power at each frequency and time point.

## Plotting

The script includes functions to plot the signal, periodogram, PSD, and spectrogram. The periodogram and PSD are plotted in dB scale using `10*np.log10(values)`. The spectrogram is plotted using `plt.pcolormesh()` with a color map of 'inferno'.

## Note on the Similarity of the Periodogram and PSD Plots

In this script, the periodogram and PSD plots look almost identical. This is because the signal is a pure 440 Hz sine wave, which is perfectly periodic. Therefore, each segment of the signal has the same frequency content, and the periodogram of each segment looks the same. When these periodograms are averaged to compute the PSD, the result is also the same.

In real-world applications, signals are often not perfectly periodic and can contain noise or other variations over time. In these cases, the periodogram of each segment can look different, and the PSD, which is the average of the periodograms, can provide a smoother and more reliable estimate of the signal's frequency content.

The method used to calculate the periodogram and PSD in this script is intended to illustrate Welch's method. There are other methods and functions available in libraries like SciPy that can compute the periodogram and PSD more efficiently. However, this script provides a step-by-step demonstration of the process, which can be helpful for understanding how these calculations work.
