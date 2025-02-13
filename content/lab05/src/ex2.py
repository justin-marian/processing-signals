""" ex2.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fftshift, fft, ifft

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

T: int = 128                                    # Number of time samples
fc: float = 20 / T                              # Cutoff frequency
fx: np.ndarray = np.linspace(-T/2, T/2 - 1, T)  # Frequency axis

a: float = 0.05                                 # Decay constant
t: np.ndarray = np.arange(T)                    # Time axis
s: np.ndarray = np.exp(-a * t)                  # Exponential decay signal

print(f"Time samples: {T}, Carrier frequency: {fc}, Decay constant: {a}")

###################################################
print(f"\n2. Computing DFT and IDFT")
print(f"=======================================\n")
###################################################

def dft(_s: np.ndarray) -> np.ndarray:
    """Discrete Fourier Transform (DFT)."""
    _N: int = len(_s)
    _S: np.ndarray = np.zeros(_N, dtype=complex)
    for _k in range(_N):
        _S[_k] = np.sum(_s * np.exp(-2j * np.pi * _k * np.arange(_N) / _N))
    return _S

def idft(_S: np.ndarray) -> np.ndarray:
    """Inverse Discrete Fourier Transform (IDFT)."""
    _N: int = len(_S)
    _s: np.ndarray = np.zeros(_N, dtype=complex)
    for _n in range(_N):
        _s[_n] = np.sum(_S * np.exp(2j * np.pi * np.arange(_N) * _n / _N)) / _N
    return _s

spectrum_dft: np.ndarray = dft(s)  # Custom DFT
spectrum: np.ndarray = fft(s)      # SciPy FFT

###################################################
print(f"\n3. Plotting Original Signal and Fourier Transform")
print(f"=======================================\n")
###################################################

def plot_signal(_t, _signal, _title, _xlabel, _ylabel, _legend):
    plt.figure(figsize=(10, 4))
    plt.plot(_t, _signal, label=_legend)
    plt.title(_title)
    plt.xlabel(_xlabel)
    plt.ylabel(_ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

plot_signal(t, s,
            r'Exponential Signal \( s(t) = e^{-at} \)',
            r'Time \( [t] \)',
            r'Amplitude',
            r'Original Signal \( s(t) \)')

def plot_spectrum(_fx, _spectrum, _title):
    plt.figure(figsize=(10, 4))
    plt.stem(_fx, np.abs(_spectrum), basefmt=" ")
    plt.title(_title)
    plt.xlabel(r'Frequency Component \( k \)')
    plt.ylabel(r'Magnitude')
    plt.grid(True)
    plt.show()

plot_spectrum(fx, spectrum_dft, r'Our DFT Model')
plot_spectrum(fx, spectrum, r'Scipy FFT Model')

###################################################
print(f"\n4. Computing and Plotting Inverse Transform")
print(f"=======================================\n")
###################################################

spectrum_shifted: np.ndarray = fftshift(spectrum)  # Shift DFT
spectrum_inverse: np.ndarray = ifft(spectrum)      # SciPy IDFT

plot_spectrum(fx, spectrum_shifted,
              r'Fourier Coefficients Before Amplitude Modulation')

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.stem(fx, np.abs(spectrum_inverse), basefmt=" ")
plt.title(r'Inverse Our IDFT (Original Signal)')
plt.xlabel(r'Frequency Component \( k \)')
plt.ylabel(r'Magnitude')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(fx, np.abs(spectrum_inverse), basefmt=" ")
plt.title(r'Inverse Scipy IFFT (Original Signal)')
plt.xlabel(r'Frequency Component \( k \)')
plt.ylabel(r'Magnitude')
plt.grid(True)
plt.show()

###################################################
print(f"\n5. Amplitude Modulation")
print(f"=======================================\n")
###################################################

carrier: np.ndarray = np.cos(2 * np.pi * fc * t)
modulated_signal: np.ndarray = (1 + s) * carrier

plot_signal(t, modulated_signal,
            r'Amplitude Modulated Signal',
            r'Time \( [t] \)',
            r'Amplitude',
            r'Modulated Signal \( (1 + s(t)) \cdot \cos(2\pi f_c t) \)')

###################################################
print(f"\n6. Computing and Plotting Modulated Signal Spectrum")
print(f"=======================================\n")
###################################################

spectrum_modulated_dft: np.ndarray = dft(modulated_signal)                  # Custom DFT
spectrum_modulated: np.ndarray = fft(modulated_signal)                      # SciPy FFT
spectrum_modulated_inverse: np.ndarray = ifft(spectrum_modulated)           # SciPy IDFT
spectrum_modulated_shifted: np.ndarray = fftshift(spectrum_modulated_dft)   # Shift DFT

plot_spectrum(fx, spectrum_modulated_shifted,
              r'Fourier Coefficients After Amplitude Modulation')

plot_signal(t, np.real(spectrum_modulated_inverse),
            r'Fourier Inverse -> back to signal',
            r'Frequency Component \( k \)',
            r'Magnitude',
            r'Inverse FFT Reconstruction')

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
