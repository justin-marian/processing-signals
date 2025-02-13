""" ex2.py """

from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

###################################################
print(f"\n1. Loading Signal Data")
print(f"=======================================\n")
###################################################

file_path: str = "../data/notes_signal.npz"
npz = np.load(file_path)

notes_signal: np.ndarray = np.array(npz['notes_signal'], dtype=np.float64)
fs: float = float(npz['fs'])  # Sampling frequency

time_axis: np.ndarray = np.arange(len(notes_signal)) / fs

print(f"Loaded signal with {len(notes_signal)} samples, Sampling Frequency: {fs} Hz")

###################################################
print(f"\n2. Plotting Original Time-Domain Signal")
print(f"=======================================\n")
###################################################

def plot_signal(time: np.ndarray, signal: np.ndarray, title: str):
    """Plots a time-domain signal."""
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, 'b-')
    plt.title(title, fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Amplitude", fontsize=12)
    plt.grid(True)
    plt.show()

plot_signal(time_axis, notes_signal, r"Original Signal")

###################################################
print(f"\n3. Computing and Plotting Frequency Spectrum")
print(f"=======================================\n")
###################################################

def compute_fft(signal: np.ndarray, sampling_rate: float) -> list[Any]:
    """Computes the FFT and frequency axis."""
    spectrum = fft(signal)
    freqs = fftfreq(len(signal), d=1 / sampling_rate)
    return [freqs[:len(signal) // 2], np.abs(spectrum)[:len(spectrum) // 2]]

def plot_spectrum(freqs: np.ndarray, spectrum: np.ndarray, title: str):
    """Plots the magnitude spectrum of a signal."""
    plt.figure(figsize=(10, 4))
    plt.stem(freqs, spectrum, basefmt=" ")
    plt.title(title, fontsize=14)
    plt.xlabel("Frequency (Hz)", fontsize=12)
    plt.ylabel("Magnitude", fontsize=12)
    plt.grid(True)
    plt.show()

freqs_original, spectrum_original = compute_fft(notes_signal, fs)
plot_spectrum(freqs_original, spectrum_original,
              r"Frequency Spectrum of the Original Signal")

###################################################
print(f"\n4. Applying Hanning Window")
print(f"=======================================\n")
###################################################

hanning_window: np.ndarray = np.hanning(len(notes_signal))
plot_signal(time_axis, hanning_window, r"Hanning Window")
windowed_signal: np.ndarray = notes_signal * hanning_window
plot_signal(time_axis, windowed_signal, r"Windowed Signal")

###################################################
print(f"\n5. Computing and Plotting Frequency Spectrum (Windowed)")
print(f"=======================================\n")
###################################################

freqs_windowed, spectrum_windowed = compute_fft(windowed_signal, fs)
plot_spectrum(freqs_windowed, spectrum_windowed,
              r"Frequency Spectrum of the Windowed Signal")

print("\nFFT Analysis with Hanning Window Completed!\n")

###################################################
print("=======================================\n")
print("\nSimulation complete!")
print("=======================================\n")
###################################################
