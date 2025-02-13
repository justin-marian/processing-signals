""" ex1.py """

import matplotlib.pyplot as plt
from fourier_series import *

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

A: float = 3        # Amplitude [-A, A]
T: int = 100        # Time interval [1, 100]
k_max: int = 20     # Max Fourier coefficients [-k_max, k_max]

print(f"Time interval: {T}")
print(f"Amplitude: {A}")
print(f"Max Fourier coefficients: {k_max}")

time_samples: np.ndarray = np.arange(1, T + 1, dtype=np.float64)
original_signal: np.ndarray = np.full(T, -A, dtype=np.float64)
original_signal[:T // 2] = A  # Assign first half as A

###################################################
print(f"\n2. Plotting Original Rectangular Signal")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(10, 4))
plt.plot(time_samples, original_signal, 'b-', linewidth=2)
plt.title(r'$\text{Original Rectangular Signal}$', fontsize=14)
plt.xlabel(r'$\text{Time} [t]$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.ylim([-A - 1, A + 1])
plt.grid(True)
plt.show()

###################################################
print(f"\n3. Computing and Plotting Fourier Coefficients")
print(f"=======================================\n")
###################################################

k_values, coefficients = dft(k_max, A)

plt.figure(figsize=(10, 4))
plt.stem(k_values, np.abs(coefficients), basefmt=" ")
plt.title(r'$\text{Magnitude of Fourier Coefficients}$', fontsize=14)
plt.xlabel(r'$k$', fontsize=12)
plt.ylabel(r'$\text{Magnitude } |c_k|$', fontsize=12)
plt.grid(True)
plt.show()

###################################################
print(f"\n4. Reconstructing and Plotting the Signal")
print(f"=======================================\n")
###################################################

reconstructed_signal = idft(time_samples, k_values, coefficients, T)

plt.figure(figsize=(10, 4))
plt.plot(time_samples, reconstructed_signal, 'r-', linewidth=2, label=r'$\text{Reconstructed Signal}$')
plt.plot(time_samples, original_signal, 'b--', linewidth=1.5, label=r'$\text{Original Signal}$')
plt.title(r'$\text{Reconstructed vs. Original Signal}$', fontsize=14)
plt.xlabel(r'$\text{Time} [t]$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

###################################################
print(f"\n5. Evaluating Different k_max Values")
print(f"=======================================\n")
###################################################

k_max_values: list[int] = [1, 5, 11, 49]

for current_k_max in k_max_values:
    print(f"Evaluating reconstruction with k_max = {current_k_max}...")

    k_values, coefficients = dft(current_k_max, A)
    reconstructed_signal = idft(time_samples, k_values, coefficients, T)

    plt.figure(figsize=(10, 4))
    plt.plot(time_samples, reconstructed_signal, 'r-', linewidth=2,
             label=fr'$\text{{Reconstructed with }} k_{{\text{{max}}}} = {current_k_max}$')
    plt.plot(time_samples, original_signal, 'b--', linewidth=1.5, label=r'$\text{Original Signal}$')
    plt.title(fr'$\text{{Reconstructed Signal with }} k_{{\text{{max}}}} = {current_k_max}$', fontsize=14)
    plt.xlabel(r'$\text{Time} [t]$', fontsize=12)
    plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
