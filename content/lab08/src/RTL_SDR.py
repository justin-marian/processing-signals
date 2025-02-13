""" RTL_SDR.py """

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fftpack import fft
from scipy.io.wavfile import write

from rtlsdr import RtlSdr
import sounddevice as sd

# File paths for input/output data
root: str = "../data"
in_file: str = f"{root}/x1.npy"
out_file: str = f"{root}/x1.wav"
out_spectrum_png: str = f"{root}/spectrum_signal.png"
out_filtered_spectrum_png: str = f"{root}/filtered_spectrum_signal.png"
out_dec_dem_png: str = f"{root}/decimated_demodulated_signal.png"
out_dem_fm_png: str = f"{root}/demodulated_signal.png"
demodulated_signal_psd: str = f"{root}/demodulated_signal_psd.png"
out_dem_fm_mono_channel_png: str = f"{root}/out_dem_fm_mono_channel_signal.png"

# Set plot configurations
plt.rcParams['figure.dpi'] = 170
plt.rcParams['figure.figsize'] = (8, 4)

# Set 1 if using an RTL-SDR device, 0 otherwise
use_sdr: int = 0

# Frequency of the radio station to tune in to
F_station: int = int(88.5e6)  # Trinitas FM frequency

# Sampling frequency and number of samples
Fs: int = 2280000  # Sampling frequency (in Hz)
N: int = 8192000   # Number of samples

# Load or capture the signal
if use_sdr == 0:
    x1: np.ndarray = np.load(in_file)
else:
    # Initialize the RTL-SDR device
    sdr: RtlSdr = RtlSdr()

    # Set parameters for the device
    sdr.sample_rate = Fs
    sdr.center_freq = F_station
    sdr.gain = 'auto'

    # Read raw signal
    x1: np.ndarray = sdr.read_samples(N)
    np.save(in_file, x1)

    # Release the device resources
    sdr.close()

# Plot the spectrogram of the signal
plt.figure()
plt.specgram(x1, NFFT=2**10, Fs=Fs)
plt.title('Spectrogram of the Signal (X1)')
plt.ylim(-Fs / 2, Fs / 2)
plt.ticklabel_format(style='plain')
plt.savefig(out_spectrum_png)
plt.close()

# FM signals are transmitted with a bandwidth of 200 kHz
f_bw: int = 200000

# Filter the signal
# Create a low-pass digital filter using scipy.signal.firwin

# 1. Select the number of taps (coefficients) for the filter (try 8, 16, 32)
ntaps: int = 32
# 2. Calculate the cutoff frequency as a ratio between the maximum frequency of interest (e.g., f_bw) and fs/2
fcut1: float = f_bw / (Fs / 2)
# 3. Choose a window function to attenuate DFT leakage from the filter (e.g., 'hamming')
# 4. Use scipy.signal.firwin to obtain the FIR filter coefficients
b: np.ndarray = signal.firwin(ntaps, fcut1, window='hamming')
# 5. Filter the initial signal (x1) with the obtained coefficients using scipy.signal.lfilter
x1f: np.ndarray = signal.lfilter(b, 1, x1)

# Plot the spectrogram of the filtered signal
plt.figure(figsize=(10, 4))
plt.specgram(x1f, NFFT=2**10, Fs=Fs)
plt.title('Spectrogram of the Signal (X1f)')
plt.ylim(-Fs / 2, Fs / 2)
plt.ticklabel_format(style='plain')
plt.savefig(out_filtered_spectrum_png)
plt.close()

# Decimation
# Decimate (subsample) the signal to have a new sampling frequency equal to f_bw (i.e., fs' = f_bw)

dec_rate: int = int(Fs / f_bw)
x2: np.ndarray = signal.decimate(x1f, dec_rate)

# New sampling frequency
Fs_new: float = Fs / dec_rate

# Plot the spectrogram of the decimated signal
plt.figure(figsize=(4, 10))
plt.specgram(x2, NFFT=2**10, Fs=Fs_new)
plt.title('Spectrogram of the Signal (X2)')
plt.ylim(-Fs_new / 2, Fs_new / 2)
plt.ticklabel_format(style='plain')
plt.savefig(out_dec_dem_png)
plt.close()

# Demodulate the FM signal
# Demodulate the FM signal using a simple frequency discriminator

# 1. Using the decimated signal (x2), obtain a delayed copy by one element (x2_int = x2[1 :])
x2_int: np.ndarray = x2[1:]
# 2. Calculate the conjugate of this delayed signal (use numpy.conj)
x2_int_conj: np.ndarray = np.conj(x2_int)
# 3. Multiply the decimated signal (x2) with the conjugated delayed signal
xx: np.ndarray = x2[:-1] * x2_int_conj
# 4. Calculate the phase (angle) of the resulting signal from the multiplication (use numpy.angle)
# The phase will be directly proportional to the transmitted signal, and can be used directly.
x3: np.ndarray = np.angle(xx)

# Visualize the obtained FM signal by displaying its power spectral density
plt.figure()
plt.psd(x3, NFFT=2048, Fs=Fs_new, color='blue')
plt.title('Decimated and Demodulated FM Signal')
plt.axvspan(0, 15000, color='red', alpha=0.2)
plt.axvspan(19000 - 500, 19000 + 500, color='green', alpha=0.2)
plt.axvspan(19000 * 2 - 15000, 19000 * 2 + 15000, color='orange', alpha=0.2)
plt.axvspan(19000 * 3 - 1500, 19000 * 3 + 1500, color='blue', alpha=0.2)
plt.savefig(demodulated_signal_psd)
plt.close()

# Calculate and display FFT of the demodulated signal

# 1. Calculate FFT from x3 using scipy.fftpack.fft
yf: np.ndarray = fft(x3)
# 2. Display the absolute value of the spectrum (np.abs) between 0 and fs/2
nf: int = len(yf)
# Note: You can use np.linspace to create a frequency vector between 0 and fs, useful for plotting
xf: np.ndarray = np.linspace(0.0, float(Fs_new), nf)
plt.figure()
plt.plot(xf[:nf//2], np.abs(yf[:nf//2]))
plt.title('FFT Spectrum of the Demodulated FM Signal')
plt.grid()
plt.savefig(out_dem_fm_png)
plt.close()

# Extract the audio signal (mono) by filtering and decimating

# 1. Filter the previous signal (x3) to retain only components between 0 and 15 kHz (corresponds to mono signal)
ntaps2: int = 32
fmaxa: int = 15000
fcut2: float = fmaxa / (Fs_new / 2)
b2: np.ndarray = signal.firwin(ntaps2, fcut2, window='hamming')
x3f: np.ndarray = signal.lfilter(b2, 1, x3)

# 2. Calculate and display FFT for the filtered signal and compare with FFT of the previous signal (unfiltered)
yff: np.ndarray = fft(x3f)
nff: int = len(yff)
xff: np.ndarray = np.linspace(0.0, float(Fs_new), nff)
plt.figure()
plt.plot(xff[:nff//2], 2.0 / nff * np.abs(yff[:nff//2]))
plt.title('FFT Spectrum of the Demodulated FM Signal after Mono Channel Filtering')
plt.grid()
plt.savefig(out_dem_fm_mono_channel_png)
plt.close()

# 3. Decimate the signal to have the final sampling frequency of f_audio = 44,100 Hz for playback
f_audio: int = 44100
dec_audio: int = int(Fs_new / f_audio)
Fs_audio: float = Fs_new / dec_audio
xa: np.ndarray = signal.decimate(x3f, dec_audio)

input("Press Enter to play audio from signal...")

# Play the signal and save it as a WAV file
xs: np.ndarray = np.int16(xa / np.max(np.abs(xa)) * 32767)
sd.play(xs, f_audio)
write(out_file, f_audio, xs)

print("Finished!\n")
input("Press Enter to continue...")
