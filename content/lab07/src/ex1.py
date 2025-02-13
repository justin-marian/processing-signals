""" ex1.py """

from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

A1: float = 1.0                 # Amplitude of first sine wave
A2: float = 0.5                 # Amplitude of second sine wave

fs: int = 8000                  # Sampling frequency (Hz)
f1: int = 1000                  # First sine wave frequency
f2: int = 2000                  # Second sine wave frequency

N: int = 8                      # Number of samples
K: int = 64                     # Total DFT samples after zero-padding
ts: float = 1 / fs              # Sampling time

n: np.ndarray = np.arange(N)    # Sample indices

print(f"Sampling Frequency: {fs} Hz, Number of Samples: {N}, DFT Length: {K}")
print(f"Frequencies: f1 = {f1} Hz, f2 = {f2} Hz")

###################################################
print(f"\n2. Generating and Plotting Sine Waves")
print(f"=======================================\n")
###################################################

def generate_signal(
        freq1: int, freq2: int,
        amp1: float, amp2: float,
        n_period: np.ndarray,
        t_sample: float
) -> tuple[float | Any, float | Any, float | Any]:
    """Generates a signal composed of two sine waves."""
    signal1 = amp1 * np.sin(2 * np.pi * freq1 * n_period * t_sample)
    signal2 = amp2 * np.sin(2 * np.pi * freq2 * n_period * t_sample)
    return signal1, signal2, signal1 + signal2

s1, s2, s = generate_signal(f1, f2, A1, A2, n, ts)

plt.figure(figsize=(10, 4))
plt.plot(n, s1, 'r--', label=r"$s_1$ (1000 Hz)")
plt.plot(n, s2, 'b-.', label=r"$s_2$ (2000 Hz)")
plt.plot(n, s, 'k-', label=r"$s_1 + s_2$")
plt.title(r"Two sine waves", fontsize=14)
plt.xlabel(r"Sample index", fontsize=12)
plt.ylabel(r"Amplitude", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

###################################################
print(f"\n3. Computing DFT and Plotting Spectrum")
print(f"=======================================\n")
###################################################

def plot_dft(signal: np.ndarray, title: str):
    """Plots the DFT of a given signal."""
    spectrum = fft(signal)
    plt.figure(figsize=(10, 4))
    plt.stem(np.abs(spectrum), basefmt=" ")
    plt.title(title, fontsize=14)
    plt.xlabel(r"DFT Frequency Index", fontsize=12)
    plt.ylabel(r"Magnitude", fontsize=12)
    plt.grid(True)
    plt.show()

plot_dft(s, r"DFT of $s_1 + s_2$")

###################################################
print(f"\n4. Testing Spectral Leakage by Modifying f1 and f2")
print(f"=======================================\n")
###################################################

# Case 1: Set f1 to 0
f1: int = 0
_, _, s_f1_0 = generate_signal(f1, f2, A1, A2, n, ts)
plot_dft(s_f1_0, r"DFT with $f_1 = 0$")

# Case 2: Change f2 to 2500 Hz
f1: int = 0
f2: int = 2500
_, _, s_leakage = generate_signal(f1, f2, A1, A2, n, ts)
plot_dft(s_leakage, r"DFT with $f_2 = 2500$ Hz (Leakage)")

###################################################
print(f"\n5. Zero-Padding Effect on DFT Resolution")
print(f"=======================================\n")
###################################################

def zero_pad_and_plot(signal: np.ndarray, pad_length: int, title: str):
    """Pads the signal with zeros and plots the DFT."""
    s_padded = np.pad(signal, (0, pad_length), 'constant')
    plot_dft(s_padded, title)

# Zero-padding (16 Samples)
zero_pad_and_plot(s, N, r"DFT with Zero-Padding (16 Samples)")

# Zero-padding (64 Samples)
zero_pad_and_plot(s, K - N, r"DFT with Zero-Padding (64 Samples)")

###################################################
print(f"\n6. Comparing DFT with Different Frequencies")
print(f"=======================================\n")
###################################################

f1: int = 0
f2: int = 2000
_, _, s_2000 = generate_signal(f1, f2, A1, A2, n, ts)
zero_pad_and_plot(s_2000, K - N, r"DFT with Zero-Padding (64 Samples) $f_2 = 2000$")

f1: int = 0
f2: int = 2500
_, _, s_2500 = generate_signal(f1, f2, A1, A2, n, ts)
zero_pad_and_plot(s_2500, K - N, r"DFT with Zero-Padding (64 Samples) $f_2 = 2500$")

print("\nDFT Analysis Completed!\n")

###################################################
print("=======================================\n")
print("\nSimulation complete!")
print("=======================================\n")
###################################################
