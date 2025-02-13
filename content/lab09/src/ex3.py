""" ex3.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz

###################################################
print(f"\n1. Defining Signal and Filter Parameters")
print(f"=======================================\n")
###################################################

fs: int = 64000                            # Sampling frequency
steps: int = 65                            # Number of filter coefficients
t: np.ndarray = np.arange(steps - 1) / fs  # Time axis
f_test: list[int] = [3000, 15000, 30000]   # Test frequencies

print(f"Sampling Frequency: {fs} Hz")
print(f"Test Frequencies: {f_test}")

###################################################
print(f"\n2. Generating Test Signals")
print(f"=======================================\n")
###################################################

sines: list[np.ndarray] = [np.sin(2 * np.pi * f * t) for f in f_test]

def plot_signal(_t: np.ndarray,
                _signals: list[np.ndarray], _filtered_signals: list[np.ndarray],
                _labels: list[str], _title: str, _colors: list[str]):
    """Generic function to plot original and filtered signals."""
    for i, f in enumerate(f_test):
        plt.figure(figsize=(10, 5))
        plt.stem(_t, _signals[i],
                 linefmt=_colors[0], markerfmt=_colors[1],
                 basefmt='r-', label=f"Original {f // 1000} kHz")
        plt.stem(_t, _filtered_signals[i],
                 linefmt=_colors[2], markerfmt=_colors[3],
                 basefmt='r-', label=_labels[0])
        plt.title(rf"{_title} ({f // 1000} kHz)")
        plt.xlabel(r"Time [s]")
        plt.ylabel(r"Amplitude")
        plt.grid()
        plt.legend()
        plt.show()

###################################################
print(f"\n3. Designing Digital FIR Filters")
print(f"=======================================\n")
###################################################

filters = {
    "Low-pass Filter": firwin(steps, cutoff=0.1),
    "Band-pass Filter": firwin(steps, cutoff=[0.2, 0.5], pass_zero="bandpass"),
    "High-pass Filter": firwin(steps, cutoff=0.75, pass_zero="highpass"),
}

filtered_signals = {name: [lfilter(b, 1, sine)[:len(t)]
                           for sine in sines] for name, b in filters.items()}

print("FIR Filters designed successfully.")

###################################################
print(f"\n4. Applying Filters to Test Signals")
print(f"=======================================\n")
###################################################

plot_signal(t, sines, filtered_signals["Low-pass Filter"], ["Low-pass Filtered"],
            "Original and Low-pass Filtered Signal", ['b-', 'bo', 'g-', 'go'])

plot_signal(t, sines, filtered_signals["Band-pass Filter"], ["Band-pass Filtered"],
            "Original and Band-pass Filtered Signal", ['g-', 'go', 'm-', 'mo'])

plot_signal(t, sines, filtered_signals["High-pass Filter"], ["High-pass Filtered"],
            "Original and High-pass Filtered Signal", ['g-', 'go', 'r-', 'ro'])

###################################################
print(f"\n5. Visualizing Filter Frequency Responses")
print(f"=======================================\n")
###################################################

for name, b in filters.items():
    freq, H = freqz(b, 1, fs=fs)
    plt.figure(figsize=(10, 5))
    plt.plot(freq, 20 * np.log10(abs(H)), label=r"$|H(f)|$")
    plt.title(f'Digital Filter Frequency Response - {name}')
    plt.xlabel(r'Frequency [Hz], from $0$ to $f_s/2$')
    plt.ylabel(r'Amplitude [dB]')
    plt.grid()
    plt.legend()
    plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
