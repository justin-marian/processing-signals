""" ex3.py """

import time
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import windows
from scipy.io.wavfile import write

###################################################
print(f"\n1. Loading Signal Data")
print(f"=======================================\n")
###################################################

IN_FILE_PATH: str = "../data/notes_signal_long.npz"
OUT_FILE_PATH: str = "../data/long_signal.wav"

npz = np.load(IN_FILE_PATH)
notes_signal_long: np.ndarray = npz['notes_signal']
fs: int = npz['fs']
T: float = len(notes_signal_long) / fs  # Signal duration

time_axis: np.ndarray = np.arange(len(notes_signal_long)) / fs

print(f"Loaded signal with {len(notes_signal_long)} samples, Sampling Frequency: {fs} Hz")

###################################################
print(f"\n2. Plotting Original Time-Domain Signal")
print(f"=======================================\n")
###################################################

def plot_signal(_time_axis: np.ndarray, _signal: np.ndarray, _title: str):
    """Generic function for plotting time-domain signals."""
    plt.figure(figsize=(10, 4))
    plt.plot(_time_axis, _signal)
    plt.title(_title, fontsize=14)
    plt.xlabel(r"$\text{Time (s)}$", fontsize=12)
    plt.ylabel(r"$\text{Amplitude}$", fontsize=12)
    plt.grid(True)
    plt.show()

plot_signal(time_axis, notes_signal_long, r"Original Long Signal")

###################################################
print(f"\n3. Computing and Plotting Frequency Spectrum")
print(f"=======================================\n")
###################################################

def compute_fft(_signal: np.ndarray, _fs: int) -> tuple[np.ndarray, np.ndarray]:
    """Computes the FFT and corresponding frequency axis."""
    spectrum = fft(_signal)
    freqs = np.fft.fftfreq(len(_signal), d=1/_fs)
    return freqs, spectrum

def plot_spectrum(_freqs: np.ndarray, _spectrum: np.ndarray, _title: str):
    """Generic function for plotting magnitude spectrum."""
    plt.figure(figsize=(10, 4))
    plt.stem(_freqs[:len(_freqs) // 2], np.abs(_spectrum)[:len(_spectrum) // 2], basefmt=" ")
    plt.title(_title, fontsize=14)
    plt.xlabel(r"$\text{Frequency (Hz)}$", fontsize=12)
    plt.ylabel(r"$\text{Magnitude}$", fontsize=12)
    plt.grid(True)
    plt.show()

freqs_long, S_long = compute_fft(notes_signal_long, fs)
plot_spectrum(freqs_long, S_long, r"Frequency Spectrum of the Long Signal")

###################################################
print(f"\n4. Applying Hanning Window and Computing FFT")
print(f"=======================================\n")
###################################################

hanning_window_long: np.ndarray = windows.hann(len(notes_signal_long))
windowed_signal_long: np.ndarray = notes_signal_long * hanning_window_long
freqs_windowed, S_windowed_long = compute_fft(windowed_signal_long, fs)

plot_spectrum(freqs_windowed, S_windowed_long, r"Frequency Spectrum of the Windowed Long Signal")

###################################################
print(f"\n5. Playing Original Signal")
print(f"=======================================\n")
###################################################

print("\nPlaying the original long signal...")
sd.play(notes_signal_long, fs)
time.sleep(T)
sd.stop()

###################################################
print(f"\n6. Saving Processed Signal as WAV")
print(f"=======================================\n")
###################################################

sound: np.ndarray = np.int16(notes_signal_long / np.max(np.abs(notes_signal_long)) * 32767)
write(OUT_FILE_PATH, np.int32(fs), sound)

print(f"\nAudio saved successfully at: {OUT_FILE_PATH}\n")

###################################################
print("=======================================\n")
print("\nSimulation complete!")
print("=======================================\n")
###################################################
