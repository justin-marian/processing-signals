""" ex1.py """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

###################################################
print(f"\n1. Performing Manual Convolution")
print(f"=======================================\n")
###################################################

# Input Signals
x: np.ndarray = np.array([1, 3, 5, 7, 5, 4, 2])
h: np.ndarray = np.array([0.1, 0.3, 0.1])

# Manual Convolution
y_manual: list[float] = []
for n in range(len(x) - len(h) + 1):
    y_n: float = sum(h[k] * x[n + k] for k in range(len(h)))
    y_manual.append(y_n)

print("Manual Convolution Result:", y_manual)

###################################################
print(f"\n2. Defining Convolution Function")
print(f"=======================================\n")
###################################################

def convolution(_x: np.ndarray, _h: np.ndarray) -> list[float]:
    """Perform discrete convolution of two 1D arrays using a manual implementation."""
    y: list[float] = []
    for i in range(len(_x) + len(_h) - 1):
        y_i: float = sum(_h[j] * _x[i - j] for j in range(len(_h)) if 0 <= i - j < len(_x))
        y.append(y_i)
    return y

###################################################
print(f"\n3. Convolution with Impulse Signal")
print(f"=======================================\n")
###################################################

h_sine: np.ndarray = np.array([0.1, 0.2, 0.2, 0.2, 0.1])
x_impulse: np.ndarray = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0])
y_impulse: np.ndarray = convolve(x_impulse, h_sine, mode='full')

plt.figure()
plt.stem(y_impulse)
plt.title(r"Convolution with Impulse Signal $y(n)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $y(n)$")
plt.grid()
plt.show()

###################################################
print(f"\n4. Convolution with Sine Wave")
print(f"=======================================\n")
###################################################

N: int = 64
fs: int = 64000
f: int = 3000
t: np.ndarray = np.arange(N) / fs
x_sine: np.ndarray = np.sin(2 * np.pi * f * t)

# Apply Convolution
y_sine: list[float] = convolution(x_sine, h_sine)

plt.figure()
plt.stem(x_sine)
plt.title(r"Input Sine Wave $x(n)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $x(n)$")
plt.grid()
plt.show()

plt.figure()
plt.stem(y_sine)
plt.title(r"Output after Convolution $y(n)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $y(n)$")
plt.grid()
plt.show()

###################################################
print(f"\n5. Convolution using np.convolve")
print(f"=======================================\n")
###################################################

h_sine_padded: np.ndarray = np.pad(h_sine, (0, len(x_sine) - len(h_sine)), 'constant')
y_np_convolve: np.ndarray = np.convolve(x_sine, h_sine, mode='full')[:N]

plt.figure()
plt.stem(y_np_convolve)
plt.title(r"Convolution with $\text{np.convolve}$ $y(n)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $y(n)$")
plt.grid()
plt.show()

###################################################
print(f"\n6. Convolution using FFT and IFFT")
print(f"=======================================\n")
###################################################

H_fft: np.ndarray = np.fft.fft(h_sine_padded, n=len(x_sine))
X_fft: np.ndarray = np.fft.fft(x_sine, n=len(x_sine))
Y_fft: np.ndarray = H_fft * X_fft
y_ifft: np.ndarray = np.real(np.fft.ifft(Y_fft))

plt.figure()
plt.stem(y_ifft[:N])
plt.title(r"IFFT of $H(f) \cdot X(f)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $y(n)$")
plt.grid()
plt.show()

###################################################
print(f"\n7. Computing Difference between FFT and np.convolve")
print(f"=======================================\n")
###################################################

difference: float = np.abs(y_ifft[:N] - y_np_convolve[:N]).max()
print("Difference between FFT and np.convolve results:", difference)

plt.figure()
plt.stem(y_np_convolve)
plt.title(r"$\text{np.convolve}$ (mode='full') Result $y(n)$")
plt.xlabel(r"Sample Index $n$")
plt.ylabel(r"Amplitude $y(n)$")
plt.grid()
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
