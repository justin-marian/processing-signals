""" ex1.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import convolve, windows

###################################################
print(f"\n1. Defining Parameters for FIR Filters")
print(f"=======================================\n")
###################################################

N: int = 256                                       # Number of points
L: int = 65                                        # Filter length

fs: float = 1                                      # Sampling frequency
fc: float = fs / 16                                # Low-pass filter cutoff frequency
fB: float = fs / 4                                 # Band-pass shift frequency

freqs: np.ndarray = fftfreq(N, d=1 / fs)           # Frequency axis for FFT
t: np.ndarray = np.linspace(0, fs, N, endpoint=False)

###################################################
print(f"\n2. Designing Ideal Low-Pass Filter")
print(f"=======================================\n")
###################################################

H_ideal: np.ndarray = np.zeros(N)
H_ideal[:N // 16] = 1
H_ideal[-N // 16:] = 1

plt.figure()
plt.plot(t, H_ideal, label=r"$\text{Ideal Frequency Response H(f)}$")
plt.title(r"$\text{Ideal Frequency Response H(f)}$")
plt.xlabel(r"$\text{Frequency}$")
plt.ylabel(r"$\text{Amplitude}$")
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n3. Computing Ideal Impulse Response")
print(f"=======================================\n")
###################################################

h_ideal: np.ndarray = np.real(ifft(H_ideal))
h_ideal = np.fft.fftshift(h_ideal)

plt.figure()
plt.plot(h_ideal, label=r"$\text{Ideal Impulse Response h}$")
plt.title(r"$\text{Ideal Impulse Response h}$")
plt.xlabel(r"$\text{Sample Index}$")
plt.ylabel(r"$\text{Amplitude}$")
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n4. Truncating Impulse Response")
print(f"=======================================\n")
###################################################

h_truncated: np.ndarray = h_ideal[N // 2 - L // 2 : N // 2 + L // 2 + 1]

plt.figure()
plt.plot(h_truncated, label=r"$\text{Truncated Impulse Response h}$", color="red")
plt.title(r"$\text{Truncated Impulse Response h (L=65)}$")
plt.xlabel(r"$\text{Sample Index}$")
plt.ylabel(r"$\text{Amplitude}$")
plt.grid()
plt.legend()
plt.show()

###################################################
print(f"\n5. Computing Frequency Response of Truncated Filter")
print(f"=======================================\n")
###################################################

spectrum_truncated: np.ndarray = fft(h_truncated, N)

plt.figure()
plt.plot(freqs[:N // 2], np.abs(spectrum_truncated[:N // 2]))
plt.title(r"$\text{Magnitude Response of Truncated h}$")
plt.xlabel(r"$\text{Frequency (Hz)}$")
plt.ylabel(r"$\text{Magnitude}$")
plt.grid()
plt.show()

###################################################
print(f"\n6. Applying Blackman Window")
print(f"=======================================\n")
###################################################

blackman_window: np.ndarray = windows.blackman(L)
h_blackman: np.ndarray = h_truncated * blackman_window
spectrum_blackman: np.ndarray = fft(h_blackman, N)

plt.figure()
plt.plot(freqs[:N // 2], np.abs(spectrum_blackman[:N // 2]))
plt.title(r"$\text{Magnitude Response with Blackman Window}$")
plt.xlabel(r"$\text{Frequency (Hz)}$")
plt.ylabel(r"$\text{Magnitude}$")
plt.grid()
plt.show()

###################################################
print(f"\n7. Designing Band-pass Filter")
print(f"=======================================\n")
###################################################

cos_seq: np.ndarray = np.cos(2 * np.pi * fB * np.arange(L) / fs)
h_bandpass: np.ndarray = h_blackman * cos_seq
spectrum_bandpass: np.ndarray = fft(h_bandpass, N)

plt.figure()
plt.plot(freqs[:N // 2], np.abs(spectrum_bandpass[:N // 2]))
plt.title(r"$\text{Magnitude Response of Band-pass Filter}$")
plt.xlabel(r"$\text{Frequency (Hz)}$")
plt.ylabel(r"$\text{Magnitude}$")
plt.grid()
plt.show()

###################################################
print(f"\n8. Designing High-pass Filter")
print(f"=======================================\n")
###################################################

h_highpass: np.ndarray = h_truncated * np.array([1 if i % 2 == 0 else -1 for i in range(len(h_truncated))])
spectrum_highpass: np.ndarray = fft(h_highpass, N)

plt.figure()
plt.plot(freqs[:N // 2], np.abs(spectrum_highpass[:N // 2]))
plt.title(r"$\text{Magnitude Response of High-pass Filter}$")
plt.xlabel(r"$\text{Frequency (Hz)}$")
plt.ylabel(r"$\text{Magnitude}$")
plt.grid()
plt.show()

###################################################
print(f"\n9. Testing Filters with Sinusoidal Signals")
print(f"=======================================\n")
###################################################

N_test: int = 65
fs_test: int = 64000
f_test: list[int] = [3000, 15000, 30000]
t_test: np.ndarray = np.arange(N_test - 1) / fs_test
sines: list[np.ndarray] = [np.sin(2 * np.pi * f * t_test) for f in f_test]

# Band-pass Filter Test
for i, f in enumerate(f_test):
    filtered_bp: np.ndarray = convolve(sines[i], h_bandpass, mode="same")

    plt.figure()
    plt.stem(t_test, sines[i],
             linefmt="g-", markerfmt="go", basefmt="r-", label=f"Original {f}Hz")
    plt.stem(t_test, filtered_bp,
             linefmt="b-", markerfmt="bo", basefmt="r-", label="Band-pass Filtered")
    plt.title(rf"$\text{{Band-pass Filtered Signal (f={f}Hz)}}$")
    plt.xlabel(r"$\text{Time (s)}$")
    plt.ylabel(r"$\text{Amplitude}$")
    plt.legend()
    plt.grid()
    plt.show()

# High-pass Filter Test
for i, f in enumerate(f_test):
    filtered_hp: np.ndarray = convolve(sines[i], h_highpass, mode="same")

    plt.figure()
    plt.stem(t_test, sines[i],
             linefmt="g-", markerfmt="go", basefmt="r-", label=f"Original {f}Hz")
    plt.stem(t_test, filtered_hp,
             linefmt="orange", markerfmt="ro", basefmt="r-", label="High-pass Filtered")
    plt.title(rf"$\text{{High-pass Filtered Signal (f={f}Hz)}}$")
    plt.xlabel(r"$\text{Time (s)}$")
    plt.ylabel(r"$\text{Amplitude}$")
    plt.legend()
    plt.grid()
    plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
