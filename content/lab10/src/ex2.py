""" ex2.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

###################################################
print(f"\n1. Defining Signal and Filter Parameters")
print(f"=======================================\n")
###################################################

N: int = 65                               # Number of samples
fs: int = 64000                           # Sampling frequency
order: int = 4                            # Filter order
f_test: list[int] = [3000, 15000, 30000]  # Test frequencies for filtering

# Time vector
t: np.ndarray = np.arange(N - 1) / fs
# Generate test sine waves
sines: list[np.ndarray] = [np.sin(2 * np.pi * f * t) for f in f_test]

print(f"Sampling Frequency: {fs} Hz")
print(f"Filter Order: {order}")
print(f"Test Frequencies: {f_test}")

###################################################
print(f"\n2. Designing Digital IIR Filters")
print(f"=======================================\n")
###################################################

# Low-pass filter
low_cutoff = 0.1 * (fs / 2)
b_low, a_low = butter(order, low_cutoff, btype='low', fs=fs)

# High-pass filter
high_cutoff = 0.75 * (fs / 2)
b_high, a_high = butter(order, high_cutoff, btype='high', fs=fs)

# Band-pass filter
band_cutoff = [0.2 * (fs / 2), 0.5 * (fs / 2)]
b_band, a_band = butter(order, band_cutoff, btype='band', fs=fs)

print("IIR Filters designed successfully.")

###################################################
print(f"\n3. Applying Filters to Test Signals")
print(f"=======================================\n")
###################################################

filtered_sines_low = [lfilter(b_low, a_low, sine)[:len(t)] for sine in sines]
filtered_sines_high = [lfilter(b_high, a_high, sine)[:len(t)] for sine in sines]
filtered_sines_band = [lfilter(b_band, a_band, sine)[:len(t)] for sine in sines]

###################################################
print(f"\n4. Visualizing Filtered Signals")
print(f"=======================================\n")
###################################################

def plot_filtered_signal(_original: np.ndarray, _filtered: np.ndarray,
                         _t: np.ndarray, _freq: int, _filter_type: str, _color: str):
    """Plot original and filtered signals."""
    plt.figure(figsize=(10, 5))
    plt.stem(t, _original,
             linefmt='g-', markerfmt='go', basefmt='r-', label=f"Original {freq // 1000} kHz")
    plt.stem(t, _filtered,
             linefmt=_color, markerfmt=_color[0]+'o', basefmt='r-', label=f"{_filter_type} Filtered")
    plt.title(rf"Original and {_filter_type} Filtered Signal ({freq // 1000} kHz)")
    plt.xlabel(r"Time [s]")
    plt.ylabel(r"Amplitude")
    plt.grid()
    plt.legend()
    plt.show()

# Plot filtered signals for each filter type
for i, freq in enumerate(f_test):
    plot_filtered_signal(sines[i], filtered_sines_low[i], t, freq, "Low-pass", 'b-')
    plot_filtered_signal(sines[i], filtered_sines_band[i], t, freq, "Band-pass", 'm-')
    plot_filtered_signal(sines[i], filtered_sines_high[i], t, freq, "High-pass", 'r-')

###################################################
print(f"\n5. Visualizing Frequency Response of Filters")
print(f"=======================================\n")
###################################################

def plot_frequency_response(_b: np.ndarray, _a: np.ndarray, _title: str):
    """Plot frequency response of a given filter."""
    _freq, _H = freqz(_b, _a, fs=fs)
    plt.figure(figsize=(10, 5))
    plt.plot(_freq, 20 * np.log10(abs(_H) + 1e-10), label=r"$|H(f)|$")
    plt.title(f'Digital Filter Frequency Response - {_title}')
    plt.xlabel(r'Frequency [Hz], from $0$ to $f_s/2$')
    plt.ylabel(r'Amplitude [dB]')
    plt.grid()
    plt.legend()
    plt.show()

# Plot frequency responses for all filters
for b, a, title in zip([b_low, b_band, b_high], [a_low, a_band, a_high],
                        ["Low-pass Filter", "Band-pass Filter", "High-pass Filter"]):
    plot_frequency_response(b, a, title)

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
