""" ex3.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Defining Signal Parameters")
print(f"=======================================\n")
###################################################

f_fundamental: int = 1  # Hz
f1: int = 1 * f_fundamental
f2: int = 2 * f_fundamental

T: np.float64 = np.float64(1 / f_fundamental)        # Fundamental period
t: np.ndarray = np.linspace(0, T, 1000)  # Time vector

print(f"Fundamental Frequency: {f_fundamental} Hz")
print(f"Period: {T} seconds")
print(f"Time vector defined with {len(t)} samples.")

###################################################
print(f"\n2. Generating Random Bit Sequence")
print(f"=======================================\n")
###################################################

random_sequence: np.ndarray = np.random.randint(0, 4, 10)
encoded_signal: np.ndarray = np.array([])

print(f"Generated random sequence: {random_sequence}")

###################################################
print(f"\n3. Encoding Signal")
print(f"=======================================\n")
###################################################

signal: np.ndarray = np.array([])

for bit_pair in random_sequence:
    if bit_pair == 0:  # '00'
        signal = np.zeros_like(t)
    elif bit_pair == 1:  # '01'
        signal = np.sin(2 * np.pi * f1 * t)
    elif bit_pair == 2:  # '10'
        signal = np.sin(2 * np.pi * f2 * t)
    elif bit_pair == 3:  # '11'
        signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Append the signal corresponding to the current bit pair
    encoded_signal = np.hstack((encoded_signal, signal))

print("Signal encoding complete.")

###################################################
print(f"\n4. Plotting Encoded Signal")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(12, 4))
time_vector: np.ndarray = np.linspace(0, len(random_sequence) * T, len(encoded_signal))
plt.plot(time_vector, encoded_signal, label=r"$\text{Encoded Signal}$")
plt.title(r'$\text{Encoded Signal for Random Sequence}$', fontsize=14)
plt.xlabel(r'$\text{Time [s]}$', fontsize=12)
plt.ylabel(r'$\text{Amplitude}$', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

print("\nEncoding and visualization complete.")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
