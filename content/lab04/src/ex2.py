""" ex2.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

A: float = 1     # Amplitude
T: int = 100     # Period
delta: int = 20  # Pulse width
kmax: int = 30   # Maximum Fourier coefficients

print(f"Amplitude: {A}")
print(f"Time interval: {T}")
print(f"Max Fourier coefficients: {kmax}")

t: np.ndarray = np.arange(0, T)  # Time vector
s: np.ndarray = np.zeros(T)      # Pulse signal
s[:delta] = 1                    # Define pulse width

###################################################
print(f"\n2. Plotting Original Pulse Signal")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(8, 6))
plt.title(r'Pulse Signal', fontsize=14)
plt.plot(t, s, color='blue', linestyle='-', linewidth=2)
plt.grid()
plt.xlabel(r'Time $t$', fontsize=12)
plt.ylabel(r'Amplitude', fontsize=12)
plt.tight_layout()
plt.show()

###################################################
print(f"\n3. Computing Fourier Coefficients")
print(f"=======================================\n")
###################################################

def ck_pulse(_A: float, _k: int, _delta: int, _T: int) -> np.float64:
    """Compute Fourier coefficient for pulse signal."""
    return _A * np.exp(-1j * (np.pi * _k * _delta) / _T) * (_delta / _T) * np.sinc((_k * _delta) / _T)

k_vals_range = range(0, kmax + 1)
ck_val = np.array([ck_pulse(A, k, delta, T) for k in k_vals_range])

plt.figure(figsize=(8, 6))
plt.title(r'Unfiltered Fourier Coefficients $c_k$', fontsize=14)
plt.stem(k_vals_range, np.abs(ck_val), basefmt=" ", markerfmt='bo', linefmt='b-')
plt.grid()
plt.xlabel(r'$k$', fontsize=12)
plt.ylabel(r'$|c_k|$', fontsize=12)
plt.tight_layout()
plt.show()

###################################################
print(f"\n4. Applying Low-Pass Filtering")
print(f"=======================================\n")
###################################################

def H_filter(_k: int, _T: int, _ck_vals: np.ndarray, _fc: float) -> np.ndarray:
    """Apply a low-pass filter to Fourier coefficients, fc = 1 / 2πRC."""
    return (1 / (1 + (1j * _k) / (_fc * _T))) * _ck_vals[_k]

fc1: float = 0.1 / T  # Cut-off frequency 0.1 / T
fc2: float = 1 / T    # Cut-off frequency 1 / T
fc3: float = 10 / T   # Cut-off frequency 10 / T

# Compute filtered Fourier coefficients
ck_filtered_1 = np.array([H_filter(k, T, ck_val, fc1) for k in k_vals_range])
ck_filtered_2 = np.array([H_filter(k, T, ck_val, fc2) for k in k_vals_range])
ck_filtered_3 = np.array([H_filter(k, T, ck_val, fc3) for k in k_vals_range])

###################################################
print(f"\n5. Plotting Filtered Fourier Coefficients")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.title(r'$f_c = \frac{0.1}{T}$', fontsize=12)
plt.stem(k_vals_range, np.abs(ck_filtered_1), basefmt=" ", markerfmt='ro', linefmt='r-')
plt.xlabel(r'$k$', fontsize=10)
plt.ylabel(r'$|c_k|$', fontsize=10)
plt.grid(True)

plt.subplot(1, 3, 2)
plt.title(r'$f_c = \frac{1}{T}$', fontsize=12)
plt.stem(k_vals_range, np.abs(ck_filtered_2), basefmt=" ", markerfmt='go', linefmt='g-')
plt.xlabel(r'$k$', fontsize=10)
plt.ylabel(r'$|c_k|$', fontsize=10)
plt.grid(True)

plt.subplot(1, 3, 3)
plt.title(r'$f_c = \frac{10}{T}$', fontsize=12)
plt.stem(k_vals_range, np.abs(ck_filtered_3), basefmt=" ", markerfmt='bo', linefmt='b-')
plt.xlabel(r'$k$', fontsize=10)
plt.ylabel(r'$|c_k|$', fontsize=10)
plt.grid(True)

plt.suptitle(r'Fourier Coefficients for Different Cut-off Frequencies', fontsize=14)
plt.tight_layout()
plt.show()

###################################################
print(f"\n6. Reconstructing Signals from Filtered Fourier Coefficients")
print(f"=======================================\n")
###################################################

def reconstruct_signal(_ck_filtered: np.ndarray, _k_vals_range: range, _T: int, _t: np.ndarray) -> np.ndarray:
    """Reconstruct the signal from the filtered Fourier coefficients."""
    _ck_conj = np.conj(_ck_filtered[1:][::-1])  # Take the conjugate of positive frequencies
    _ck_final = np.concatenate([_ck_conj, _ck_filtered])  # Combine negative and positive frequencies
    _k_vals_final = np.arange(-len(_ck_conj), len(_ck_filtered))  # Define k values symmetrically

    _s_rec = np.zeros(len(_t), dtype=complex)
    for _i, _k in enumerate(_k_vals_final):
        _s_rec += _ck_final[_i] * np.exp((1j * 2 * np.pi * np.real(_k) * _t) / _T)

    return np.real(_s_rec)

# Compute reconstructed signals
s_rec_1 = reconstruct_signal(np.complex64(ck_filtered_1), k_vals_range, T, t)
s_rec_2 = reconstruct_signal(np.complex64(ck_filtered_2), k_vals_range, T, t)
s_rec_3 = reconstruct_signal(np.complex64(ck_filtered_3), k_vals_range, T, t)

###################################################
print(f"\n7. Plotting Reconstructed Signals")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(10, 6))
plt.plot(t, s, label='Original Pulse Signal', color='blue', linewidth=2)
plt.plot(t, s_rec_1, label=r'$f_c = \frac{0.1}{T}$', color='orange', linestyle='--', linewidth=2)
plt.plot(t, s_rec_2, label=r'$f_c = \frac{1}{T}$', color='green', linestyle='--', linewidth=2)
plt.plot(t, s_rec_3, label=r'$f_c = \frac{10}{T}$', color='red', linestyle='--', linewidth=2)
plt.title(r'Reconstructed Signals with Different Cutoff Frequencies', fontsize=14)
plt.xlabel(r'Time $t$', fontsize=12)
plt.ylabel(r'Amplitude', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nPulse Signal Filtering and Reconstruction Completed.")


###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
