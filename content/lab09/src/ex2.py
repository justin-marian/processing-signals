""" ex2.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import windows
from scipy.fft import fft, ifft, fftfreq, ifftshift

###################################################
print(f"\n1. Defining Parameters for FIR Filter")
print(f"=======================================\n")
###################################################

N: int = 256                                  # Total number of points
fs: float = 64000.0                           # Sampling frequency
fc: float = fs / 16                           # Cutoff frequency
fcs: list[float] = [fs / 2, fs / 4, fs / 16]  # Different cutoff frequencies for comparison

freqs: np.ndarray = fftfreq(N, d=1 / fs)

###################################################
print(f"\n2. Designing Ideal Low-pass Filter")
print(f"=======================================\n")
###################################################

H_ideal: np.ndarray = np.zeros(N)
cutoff_index: int = int(N * (fc / fs))
H_ideal[:cutoff_index] = 1
H_ideal[-cutoff_index:] = 1

plt.figure()
plt.plot(freqs, H_ideal, label=r'Ideal Low-pass Filter')
plt.title(r'Ideal Low-pass Filter Spectrum $H(f)$')
plt.xlabel(r'Frequency (Hz)')
plt.ylabel(r'Amplitude')
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n3. Computing Ideal Impulse Response")
print(f"=======================================\n")
###################################################

h_ideal: np.ndarray = ifftshift(ifft(H_ideal))
h_ideal = np.real(h_ideal)

plt.figure()
plt.plot(h_ideal, label=r'Ideal Impulse Response $h(n)$')
plt.title(r'Ideal Impulse Response (Time Domain)')
plt.xlabel(r'Sample Index $n$')
plt.ylabel(r'Amplitude $h(n)$')
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n4. Truncating the Impulse Response")
print(f"=======================================\n")
###################################################

L: int = 65                   # Truncation length (number of filter coefficients)
center: int = N // 2          # Center index
start: int = center - L // 2  # Start of truncation
end: int = start + L          # End of truncation

if (end - start) != L:
    raise ValueError("[ERROR]: Truncation length mismatch!")

h_truncated: np.ndarray = h_ideal[start:end]

plt.figure()
plt.plot(h_truncated,
         label=r'Truncated Impulse Response $h(n)$', color='red')
plt.title(r'Truncated Impulse Response (65 Coefficients)')
plt.xlabel(r'Sample Index $n$')
plt.ylabel(r'Amplitude $h(n)$')
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n5. Applying Blackman Window")
print(f"=======================================\n")
###################################################

blackman_window: np.ndarray = windows.blackman(L)
h_blackman: np.ndarray = h_truncated * blackman_window

plt.figure()
plt.plot(h_blackman,
         label=r'Blackman-Windowed $h(n)$', color='green')
plt.title(r'Blackman-Windowed Impulse Response (Time Domain)')
plt.xlabel(r'Sample Index $n$')
plt.ylabel(r'Amplitude $h(n)$')
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n6. Computing Frequency Response using FFT")
print(f"=======================================\n")
###################################################

H_blackman: np.ndarray = fft(h_blackman, N)

plt.figure(figsize=(10, 6))
plt.plot(freqs, np.abs(H_blackman),
         label=r'Blackman Filter Magnitude Response')

plt.title(r'Magnitude Response of Blackman-Windowed Filter')
plt.xlabel(r'Frequency (Hz)')
plt.ylabel(r'Magnitude $|H(f)|$')
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n7. Comparing Different Cutoff Frequencies")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(10, 6))

for fc in fcs:
    H_ideal: np.ndarray = np.zeros(N)
    cutoff_index: int = int(N * (fc / fs))
    H_ideal[:cutoff_index] = 1
    H_ideal[-cutoff_index:] = 1

    h_ideal: np.ndarray = ifftshift(ifft(H_ideal))
    h_ideal = np.real(h_ideal)
    h_truncated: np.ndarray = h_ideal[start:end]

    blackman_window: np.ndarray = windows.blackman(L)
    h_blackman: np.ndarray = h_truncated * blackman_window

    H_blackman: np.ndarray = fft(h_blackman, N)
    plt.plot(freqs, np.abs(H_blackman),
             label=fr'Cutoff Frequency $f_c = {fc} \, \mathrm{{Hz}}$')

plt.title(r'Magnitude Responses for Different Cutoff Frequencies')
plt.xlabel(r'Frequency (Hz)')
plt.ylabel(r'Magnitude $|H(f)|$')
plt.grid()
plt.legend()
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
