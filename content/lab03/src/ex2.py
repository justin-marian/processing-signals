""" ex2.py """

import matplotlib.pyplot as plt
from fourier_series import *

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

T: int = 100                # Period
A: float = 1                # Amplitude [-A, A]
k_max: int = 500            # Maximum number of Fourier terms
threshold: float = 0.05     # Threshold for RMS error

print(f"Period: {T}, Amplitude: {A}, k_max: {k_max}, Threshold: {threshold}")

t: np.ndarray = np.arange(1, T + 1, dtype=np.float64)       # Time samples
original_signal: np.ndarray = np.zeros(T, dtype=np.float64)
original_signal[:T // 2] = A                                # Assign first half to A
original_signal[T // 2:] = -A                               # Assign second half to -A

###################################################
print(f"\n2. Plotting Original Rectangular Signal")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(10, 4))
plt.plot(t, original_signal, 'b-', linewidth=2)
plt.title(r'$\text{Original Rectangular Signal}$', fontsize=14)
plt.xlabel(r'$\text{Time }[t]$', fontsize=12)
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
plt.stem(k_values, np.abs(coefficients) ** 2, basefmt=" ")
plt.title(r'$\text{Magnitude of Fourier Coefficients } |c_k|^2$', fontsize=14)
plt.xlabel(r'$k$', fontsize=12)
plt.ylabel(r'$\text{Magnitude } |c_k|^2$', fontsize=12)
plt.grid(True)
plt.show()

###################################################
print(f"\n4. Computing and Plotting RMS Error")
print(f"=======================================\n")
###################################################

rms_error_values: np.ndarray = rms_error(coefficients, k_max)

plt.figure(figsize=(10, 4))
plt.plot(np.arange(1, k_max + 1), rms_error_values, label=r'$\text{RMS Error}$')
plt.title(r'$\text{RMS Error as a Function of } N$', fontsize=14)
plt.xlabel(r'$N$', fontsize=12)
plt.ylabel(r'$\text{RMS Error}$', fontsize=12)
plt.grid(True)
plt.show()

###################################################
print(f"\n5. Logarithmic RMS Error Plots")
print(f"=======================================\n")
###################################################

positive_indices = np.arange(1, k_max + 1)

# SEMILOGY plot
plt.figure(figsize=(10, 4))
plt.semilogy(positive_indices, rms_error_values, label=r'$\text{RMS Error}$')
plt.title(r'$\text{RMS Error as a Function of } N$', fontsize=14)
plt.xlabel(r'$N$', fontsize=12)
plt.ylabel(r'$\text{RMS Error (log scale)}$', fontsize=12)
plt.grid(True)
plt.show()

# LOGLOG plot
plt.figure(figsize=(10, 4))
plt.loglog(positive_indices, rms_error_values, label=r'$\text{RMS Error}$')
plt.title(r'$\text{RMS Error (loglog) as a Function of } N$', fontsize=14)
plt.xlabel(r'$N$', fontsize=12)
plt.ylabel(r'$\text{RMS Error (loglog scale)}$', fontsize=12)
plt.grid(True)
plt.show()

###################################################
print(f"\n6. Computing Optimal N for Threshold")
print(f"=======================================\n")
###################################################

optimal_N: int = np.argmax(rms_error_values < threshold) + 1
print(fr"The smallest N such that rms(epsilon[N-1]) < 0.05 is {optimal_N}")

###################################################
print(f"\n7. Reconstructing and Plotting Signal with Optimal N")
print(f"=======================================\n")
###################################################

k_values, coefficients = dft(optimal_N, A)
reconstructed_signal = idft(t, k_values, coefficients, T)

plt.figure(figsize=(10, 4))
plt.plot(t, reconstructed_signal, 'r-', linewidth=2, label=fr'$\text{{Reconstructed Signal }}(N={optimal_N})$')
plt.plot(t, original_signal, 'b--', linewidth=1.5, label=r'$\text{Original Signal}$')
plt.title(fr'$\text{{Reconstructed vs. Original Signal }}(N={optimal_N})$', fontsize=14)
plt.xlabel(r'$\text{Time }[t]$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

print("\nFourier Series Analysis with RMS Error Complete.")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
