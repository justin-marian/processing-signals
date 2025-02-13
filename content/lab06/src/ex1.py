""" ex1.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftshift


def dft(_s: np.ndarray) -> np.ndarray:
    """Efficient Discrete Fourier Transform (DFT) using vectorized NumPy operations."""
    _K: int = len(_s)
    _n = np.arange(_K)
    _k = _n.reshape((_K, 1))
    exponent = np.exp(-2j * np.pi * _k * _n / _K)
    return np.dot(exponent, _s)


def idft(_S: np.ndarray) -> np.ndarray:
    """Efficient Inverse Discrete Fourier Transform (IDFT)."""
    _K: int = len(_S)
    _n = np.arange(_K)
    _k = _n.reshape((_K, 1))
    exponent = np.exp(2j * np.pi * _k * _n / _K)
    return np.dot(exponent, _S) / _K


file_path: str = '../data/noisy_signal.npz'
data: np.lib.npyio.NpzFile = np.load(file_path)
noisy_signal: np.ndarray = data['noisy_signal']

# Plot Noisy Signal
plt.figure(figsize=(10, 4))
plt.plot(noisy_signal, label=r'$\text{Noisy Signal}$')
plt.title(r'$\text{Noisy Signal}$')
plt.xlabel(r'$\text{Sample}$')
plt.ylabel(r'$\text{Amplitude}$')
plt.legend()
plt.grid(True)
plt.show()

# DFT and FFT
dft_result: np.ndarray = dft(noisy_signal)
fft_result: np.ndarray = fft(noisy_signal)

# Magnitude Spectrum
half_idx = len(dft_result) // 2
dft_magnitude = np.abs(dft_result[:half_idx])
fft_magnitude = np.abs(fft_result[:half_idx])

plt.figure(figsize=(10, 4))
plt.stem(dft_magnitude,
         basefmt=" ", linefmt='c-', markerfmt='co', label=r'$\text{Manual DFT}$')
plt.stem(fft_magnitude,
         basefmt=" ", linefmt='b--', markerfmt='bo', label=r'$\text{FFT}$')
plt.title(r'$\text{DFT vs FFT Magnitude (Positive Frequencies Only)}$')
plt.xlabel(r'$\text{Frequency Bin}$')
plt.ylabel(r'$\text{Magnitude}$')
plt.legend()
plt.grid(True)
plt.show()

# FFT Shifted Spectrum
dft_shifted = fftshift(np.abs(dft_result))
fft_shifted = fftshift(np.abs(fft_result))

plt.figure(figsize=(10, 4))
plt.stem(dft_shifted,
         basefmt=" ", linefmt='c-', markerfmt='co', label=r'$\text{Manual DFT}$')
plt.stem(fft_shifted,
         basefmt=" ", linefmt='b--', markerfmt='bo', label=r'$\text{FFT}$')
plt.title(r'$\text{FFT Shifted}$')
plt.xlabel(r'$\text{Frequency Bin}$')
plt.ylabel(r'$\text{Magnitude}$')
plt.legend()
plt.grid(True)
plt.show()

# Define Frequency Bins for Filtering
keep_freqs = 10
filtered_dft: np.ndarray = np.copy(dft_result)
filtered_fft: np.ndarray = np.copy(fft_result)

# Apply Low-Pass Filter (Keep 10 frequencies)
filtered_dft[keep_freqs:-keep_freqs] = 0
filtered_fft[keep_freqs:-keep_freqs] = 0

# Compute SNR
signal_power = np.sum(np.abs(filtered_dft[:keep_freqs]) ** 2) / keep_freqs
noise_power = np.sum(np.abs(filtered_dft[keep_freqs:]) ** 2) / (len(dft_result) - keep_freqs)
snr = signal_power / noise_power
snr_db = 10 * np.log10(snr)

print(f"Signal Power: {signal_power:.4f} W")
print(f"Noise Power: {noise_power:.4f} W")
print(f"SNR: {snr:.4f}")
print(f"SNR (in dB): {snr_db:.4f} dB(s)")

# Plot Filtered Magnitude Spectrum
plt.figure(figsize=(10, 4))
plt.stem(np.abs(filtered_dft), basefmt=" ",
         label=r'$\text{Filtered Signal (DFT)}$', linefmt='c-', markerfmt='co')
plt.stem(np.abs(filtered_fft), basefmt=" ",
         label=r'$\text{Filtered Signal (FFT)}$', linefmt='b--', markerfmt='bo')
plt.title(r'$\text{Filtered DFT Magnitude}$')
plt.xlabel(r'$\text{Frequency Bin}$')
plt.ylabel(r'$\text{Magnitude}$')
plt.legend()
plt.grid(True)
plt.show()

# Reconstruct the Signal
reconstructed_signal_idft: np.ndarray = np.real(idft(filtered_dft))
reconstructed_signal_ifft: np.ndarray = np.real(ifft(filtered_dft))

plt.figure(figsize=(10, 4))
plt.plot(reconstructed_signal_idft,
         label=r'$\text{Reconstructed Signal (IDFT)}$', linewidth=2, linestyle='-')
plt.plot(reconstructed_signal_ifft,
         label=r'$\text{Reconstructed Signal (IFFT)}$', linewidth=2, linestyle='--')
plt.plot(noisy_signal,
         label=r'$\text{Original Noisy Signal}$', linestyle=':', linewidth=1.5)
plt.title(r'$\text{Reconstructed Signal vs Original Noisy Signal}$')
plt.xlabel(r'$\text{Sample}$')
plt.ylabel(r'$\text{Amplitude}$')
plt.legend()
plt.grid(True)
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
