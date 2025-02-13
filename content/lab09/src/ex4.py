""" ex4.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, kaiserord, firwin, freqz, lfilter

###################################################
print("\n1. Defining Signal and Filter Parameters")
print("=======================================\n")
###################################################

fs: int = 48000          # Sampling frequency
fc: int = 10000          # Cutoff frequency
N_fir: int = 10          # Order of FIR filter
N_iir: int = 5           # Order of IIR filter (typically lower than FIR)
A_1: float = 1.0         # Amplitude of 1st sinusoid
A_2: float = 0.5         # Amplitude of 2nd sinusoid
n_1: int = 3000          # Frequency of 1st sinusoid
n_2: int = 15000         # Frequency of 2nd sinusoid

print(f"Sampling Frequency: {fs} Hz")
print(f"Cutoff Frequency: {fc} Hz")
print(f"Test Frequencies: {n_1} Hz, {n_2} Hz")

###################################################
print("\n2. Designing Digital FIR and IIR Filters")
print("=======================================\n")
###################################################

# FIR Filter Design using Kaiser Window
ripple_db: float = 60.0                # Attenuation in dB
width: float = 2000.0 / fs             # Transition width (normalized)
N, beta = kaiserord(ripple_db, width)  # Compute order & beta
fir_coeffs: np.ndarray = firwin(N_fir + 1, fc / (0.5 * fs), window=("kaiser", beta))

# Ensure filter order is an integer
N_iir = int(N_iir)

# Validate cutoff frequency
if not (0 < fc / (0.5 * fs) < 1):
    raise ValueError("Cutoff frequency must be between 0 and 1 after normalization.")

# IIR Filter Design (Butterworth and Chebyshev Type I)
b_butter, a_butter = butter(N_iir, fc / (0.5 * fs), btype='low')
b_cheby, a_cheby = cheby1(N_iir, 0.5, fc / (0.5 * fs), btype='low')


print("FIR and IIR filters designed successfully.")

###################################################
print("\n3. Generating Test Signal")
print("=======================================\n")
###################################################

t: np.ndarray = np.linspace(0.0, 1.0, fs, endpoint=False)
test_signal: np.ndarray = A_1 * np.sin(2 * np.pi * n_1 * t) + A_2 * np.sin(2 * np.pi * n_2 * t)

# Plot test signal
plt.figure(figsize=(12, 6))
plt.plot(t[:1000], test_signal[:1000], label="Original Signal")
plt.title("Test Signal (Combination of Two Sinusoids)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

###################################################
print("\n4. Applying Filters to the Test Signal")
print("=======================================\n")
###################################################

filtered_fir: np.ndarray = lfilter(fir_coeffs, np.array([1]), test_signal)
filtered_butter: np.ndarray = lfilter(b_butter, a_butter, test_signal)
filtered_cheby: np.ndarray = lfilter(b_cheby, a_cheby, test_signal)

###################################################
print("\n5. Visualizing Frequency Responses of Filters")
print("=======================================\n")
###################################################

def plot_frequency_response(_b: np.ndarray, _a: np.ndarray, _title: str) -> None:
    """Plot frequency response of FIR/IIR filters."""
    _w, _h = freqz(_b, _a, worN=8000)
    plt.plot((_w / np.pi) * (fs / 2), 20 * np.log10(np.abs(_h)), label=_title)

plt.figure(figsize=(12, 8))
plot_frequency_response(fir_coeffs, np.array([1]), "FIR (Kaiser Window)")
plot_frequency_response(b_butter, a_butter, "IIR (Butterworth)")
plot_frequency_response(b_cheby, a_cheby, "IIR (Chebyshev Type I)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(True)
plt.title("Frequency Response of Filters")
plt.legend()
plt.show()

###################################################
print("\n6. Comparing Filtered Signals")
print("=======================================\n")
###################################################

plt.figure(figsize=(12, 8))
plt.plot(t, test_signal, label="Original Signal", alpha=0.75)
plt.plot(t, filtered_fir, label="FIR Filtered Signal (Kaiser)", alpha=0.75)
plt.plot(t, filtered_butter, label="IIR Filtered Signal (Butterworth)", alpha=0.75)
plt.plot(t, filtered_cheby, label="IIR Filtered Signal (Chebyshev Type I)", alpha=0.75)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Signal Filtering")
plt.legend()
plt.grid(True)
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
