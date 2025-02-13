""" ex1.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

A: float = 1                                      # Amplitude
N: int = 128                                      # Number of samples
fs: float = 1000                                  # Sampling frequency (Hz)
frequencies: list[int] = [1, 2, 10, 20, 100]      # Different signal frequencies
t: np.ndarray = np.linspace(0, 1, N)   # Discrete time

print(f"Amplitude: {A}, Number of Samples: {N}, Sampling Frequency: {fs}")
print(f"Frequencies of sinusoids: {frequencies}")

###################################################
print(f"\n2. Generating and Processing Sinusoidal Signals")
print(f"=======================================\n")
###################################################

def process_signal(_input_signal: np.ndarray) -> np.ndarray:
    """Process the input signal with a moving average filter."""
    _N: int = len(_input_signal)
    _output_signal: np.ndarray = np.zeros(_N)
    for _n in range(4, _N):
        _output_signal[_n] = np.mean(_input_signal[_n - 4:_n + 1])
    return _output_signal

sinusoids: list[np.ndarray] = [A * np.sin(2 * np.pi * f * t) for f in frequencies]
processed_sinusoids: list[np.ndarray] = [process_signal(s) for s in sinusoids]

def plot_signals(_t, _signals, _titles, _labels, colors):
    for i, signal in enumerate(_signals):
        plt.figure(figsize=(12, 6))
        plt.plot(_t, signal, color=colors[i], label=_labels[i])
        plt.title(_titles[i])
        plt.xlabel(r'Time \( t \) [s]')
        plt.ylabel(r'Amplitude')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

plot_signals(t, sinusoids,
             [rf'Sinusoidal Signal at {f} Hz' for f in frequencies],
             [rf'Input Sinusoid at {f} Hz' for f in frequencies],
             ['b'] * len(frequencies))

plot_signals(t, processed_sinusoids,
             [rf'Processed Signal at {f} Hz' for f in frequencies],
             [rf'Processed Output at {f} Hz' for f in frequencies],
             ['r'] * len(frequencies))

###################################################
print(f"\n3. Adding Noise and Processing Noisy Sinusoids")
print(f"=======================================\n")
###################################################

noise_mean: float = 0.0
noise_std: float = 0.1

# Generate and process noisy sinusoids
noisy_sinusoids: list[np.ndarray] = [s + np.random.normal(noise_mean, noise_std, s.shape) for s in sinusoids]
processed_noisy_sinusoids: list[np.ndarray] = [process_signal(ns) for ns in noisy_sinusoids]

plot_signals(t, noisy_sinusoids,
             [rf'Noisy Input at {f} Hz' for f in frequencies],
             [rf'Noisy Input Sinusoid at {f} Hz' for f in frequencies],
             ['b'] * len(frequencies))

plot_signals(t, processed_noisy_sinusoids,
             [rf'Processed Noisy Signal at {f} Hz' for f in frequencies],
             [rf'Processed Output of Noisy Signal at {f} Hz' for f in frequencies],
             ['r'] * len(frequencies))

###################################################
print(f"\n4. Applying Linear Filtering using lfilter()")
print(f"=======================================\n")
###################################################

b: np.ndarray = np.ones(5) / 5
a: np.ndarray = np.array(1)

lfilter_outputs: list[np.ndarray] = [lfilter(b, a, pns) for pns in processed_noisy_sinusoids]

plot_signals(t, lfilter_outputs,
             [rf'lfilter Output at {f} Hz' for f in frequencies],
             [rf'lfilter Output at {f} Hz' for f in frequencies],
             ['r'] * len(frequencies))

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
