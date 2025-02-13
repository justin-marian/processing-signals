""" ex1.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

A: float = 1                                                # Amplitude
T: int = 100                                                # Fundamental period
tau: float = T / 4                                          # Delay of T/4
kmax: int = 81                                              # Maximum Fourier coefficients

print(f"Amplitude: {A}")
print(f"Time interval: {T}")
print(f"Time delay: {tau}")
print(f"Max Fourier coefficients: {kmax}")

k_vals: np.ndarray = np.arange(-kmax, kmax + 1, dtype=int)  # Fourier coefficient indices

t: np.ndarray = np.linspace(0, T, T)                  # Discrete time

# Rectangular signal
s: np.ndarray = np.zeros(T)
s[: T // 2] = A
s[T // 2:] = -A

t_delayed: np.ndarray = t + tau                             # Delayed time vector

# Delayed rectangular signal
s_delayed: np.ndarray = np.zeros(T)
s_delayed[: T // 2] = A
s_delayed[T // 2:] = -A

###################################################
print(f"\n2. Plotting Rectangular Signal and Delayed Signal")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(8, 6))
plt.title(r'$\text{Rectangular Signal and Delayed Signal}$', fontsize=14)
plt.plot(t, s, color='green', linestyle="--", linewidth=2, label='Original Signal')
plt.plot(t_delayed, s_delayed, color='blue', linestyle='--', linewidth=2, label='Delayed Signal (T/4)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.xlabel(r'$\text{Time [t]}$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.ylim(-A - 1, A + 1)
plt.show()

###################################################
print(f"\n3. Computing Fourier Coefficients")
print(f"=======================================\n")
###################################################

# Fourier coefficients for undelayed signal
ck_val: np.ndarray = np.zeros(len(k_vals), dtype=np.complex128)

for i in range(len(k_vals)):
    k_int: int = int(k_vals[i])
    if k_int % 2 == 0:
        ck_val[i] = 0
    else:
        ck_val[i] = (2 * A) / (1j * np.pi * k_int)

# Fourier coefficients for delayed signal (applying time shift property)
ck_delayed_val: np.ndarray = np.zeros(len(k_vals), dtype=np.complex128)

for i in range(len(k_vals)):
    k_int: int = int(k_vals[i])
    if k_int % 2 == 0:
        ck_delayed_val[i] = 0
    else:
        ck_delayed_val[i] = ck_val[i] * np.exp((-1j * 2 * np.pi * k_int) * (tau / T))

###################################################
print(f"\n4. Plotting Fourier Coefficients (Undelayed and Delayed)")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(8, 6))
plt.title(r'$\text{Fourier Coefficients (Undelayed and Delayed)}$', fontsize=14)
plt.stem(k_vals, np.abs(ck_val), basefmt=" ", markerfmt='ro', linefmt='r-', label='Undelayed')
plt.stem(k_vals, np.abs(ck_delayed_val), basefmt=" ", markerfmt='bo', linefmt='b--', label='Delayed')
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel(r'$\text{k}$', fontsize=12)
plt.ylabel(r'$\text{|C_k|}$', fontsize=12)
plt.show()

###################################################
print(f"\n5. Plotting Phase of Fourier Coefficients")
print(f"=======================================\n")
###################################################

phase_undelayed: np.ndarray = np.angle(ck_val, deg=True)
phase_delayed: np.ndarray = np.angle(ck_delayed_val, deg=True)

plt.figure(figsize=(8, 6))
plt.title(r'$\text{Phase (Undelayed and Delayed)}$', fontsize=14)
plt.stem(k_vals, phase_undelayed, basefmt=" ", markerfmt='ro', linefmt='r-', label='Undelayed')
plt.stem(k_vals, phase_delayed, basefmt=" ", markerfmt='bo', linefmt='b--', label='Delayed')
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel(r'$\text{k}$', fontsize=12)
plt.ylabel(r'$\text{Phase (degrees)}$', fontsize=12)
plt.show()

###################################################
print(f"\n6. Reconstructing Signal from Fourier Coefficients")
print(f"=======================================\n")
###################################################

s_rec_delayed: np.ndarray = np.zeros(T, dtype=np.complex128)
s_rec_undelayed: np.ndarray = np.zeros(T, dtype=np.complex128)

for i in range(len(k_vals)):
    k_int: int = int(k_vals[i])
    s_rec_delayed += ck_delayed_val[i] * np.exp((1j * 2 * np.pi * k_int * t) / T)
    s_rec_undelayed += ck_val[i] * np.exp((1j * 2 * np.pi * k_int * t) / T)

###################################################
print(f"\n7. Plotting Reconstructed Signals")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(8, 6))
plt.title(r'$\text{Reconstructed and Original Signal}$', fontsize=14)
plt.plot(t, np.real(s_rec_delayed),
         label=r'$s(t - \tau)$ Shifted Signal', linestyle='--', color='blue', linewidth=2)
plt.plot(t, np.real(s_rec_undelayed),
         label=r'$s(t)$ Original Signal', linestyle='--', color='red', linewidth=2)
plt.plot(t, s, label=r'Original Signal', linestyle="-", color='green', linewidth=3)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.ylim(-A - 1, A + 1)
plt.xlabel(r'$\text{Time }[t]$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.show()

print("\nFourier Analysis with Time Delay Completed.")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
