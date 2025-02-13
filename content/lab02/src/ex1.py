""" ex1.py """

from math import gcd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

###################################################
print(f"\n1. Signal Generation")
print(f"=======================================\n")
###################################################

f1: int = 1600  # Hz
f2: int = 1800  # Hz

print(f"Defined frequencies: f1 = {f1} Hz, f2 = {f2} Hz")

# Fundamental period
T: float = 1 / gcd(f1, f2)
T_float: np.float64 = np.float64(T)

print(f"Computed fundamental period: T = {T:.4f} s")

# Time interval for plotting
t: np.ndarray = np.linspace(0, T_float, 1000)

###################################################
print(f"\n2. Generating Signals")
print(f"=======================================\n")
###################################################

print("Generating signals with different combinations of f1 and f2...")

# Generate signals for 3 cases
x1: np.ndarray = 0 * np.sin(2 * np.pi * f1 * t) + 1 * np.sin(2 * np.pi * f2 * t)  # Only f2 component
x2: np.ndarray = 1 * np.sin(2 * np.pi * f1 * t) + 1 * np.sin(2 * np.pi * f2 * t)  # Both frequencies
x3: np.ndarray = 1 * np.sin(2 * np.pi * f1 * t) + 0 * np.sin(2 * np.pi * f2 * t)  # Only f1 component

# Concatenate all 3 signals
x_total: np.ndarray = np.hstack([x1, x2, x3])
t_total: np.ndarray = np.linspace(0, 3 * T_float, len(x_total))

###################################################
print(f"\n3. Plotting Signals")
print(f"=======================================\n")
###################################################

print("Plotting combined signal over the three cases...")

plt.figure(figsize=(10, 6))
plt.plot(t_total, x_total, label=r'$\text{Modem Signal}$', color='blue')
plt.title(r'$\text{Product Over 3 Signals of Transmission}$', fontsize=16)
plt.xlabel(r'$\text{Time [s]}$', fontsize=14)
plt.ylabel(r'$\text{Amplitude}$', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

print(f'Minimum transmission time: {T:.6f} s')

###################################################
print(f"\n4. Frequency Spectrum Analysis")
print(f"=======================================\n")
###################################################

print("Computing and plotting frequency spectrum using FFT...")

Fs = 10 * max(f1, f2)       # Sampling frequency
N = len(x_total)            # Number of samples
freqs = fftfreq(N, 1/Fs)    # Frequency axis
X_f = fft(x_total)          # Signal Spectrum

plt.figure(figsize=(10, 5))
plt.plot(freqs[:N // 2], np.abs(X_f[:N // 2]), color='red')
plt.title(r'$\text{Frequency Spectrum of Transmission Signal}$', fontsize=16)
plt.xlabel(r'$\text{Frequency [Hz]}$', fontsize=14)
plt.ylabel(r'$\text{Magnitude}$', fontsize=14)
plt.grid(True)
plt.show()

print("Frequency spectrum analysis complete.")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
