""" ex3.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Generating Complex Exponentials")
print(f"=======================================\n")
###################################################

# Time sequences 0, pi/6, pi/4, pi/3, pi/2
t: np.ndarray = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])

print("Defined sequence t:", t)

s1: np.ndarray = np.exp(1j * t)   # e^(j * t)
s2: np.ndarray = np.exp(-1j * t)  # e^(-j * t)

print("Computed complex exponentials: e^(j*t) and e^(-j*t)")

###################################################
print(f"\n2. Plotting in the Complex Plane")
print(f"=======================================\n")
###################################################

print("Plotting complex exponentials in the complex plane...")

plt.figure(figsize=(10, 12))

x_complex_exp1: np.ndarray = np.real(s1)
y_complex_exp1: np.ndarray = np.imag(s1)
plt.plot(x_complex_exp1, y_complex_exp1, 'ro', label=r'$\text{e}^{j \cdot t}$')

x_complex_exp2: np.ndarray = np.real(s2)
y_complex_exp2: np.ndarray = np.imag(s2)
plt.plot(x_complex_exp2, y_complex_exp2, 'bo', label=r'$\text{e}^{-j \cdot t}$')

ss: np.ndarray = (s1 + s2) / 2  # cos(t) = (e^(j * t) + e^(-j * t)) / 2
x_complex_ss: np.ndarray = np.real(ss)
y_complex_ss: np.ndarray = np.imag(ss)

plt.plot(x_complex_ss, y_complex_ss, 'go', label=r'$\cos(t)$ from average')
plt.xlabel(r'$\text{Real Part}$', fontsize=14)
plt.ylabel(r'$\text{Imaginary Part}$', fontsize=14)
plt.title(r'$\text{Complex Exponentials and cos(t) in } \mathbb{C} \text{ Plane}$', fontsize=16)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

print("Complex plane visualization complete.")

###################################################
print(f"\n3. Computing and Plotting sin(t)")
print(f"=======================================\n")
###################################################

print("Computing sin(t) from the imaginary part of e^(j*t)...")

sin_t: np.ndarray = np.imag(s1)

print("Plotting sin(t)...")

plt.figure()
plt.plot(t, sin_t, 'ms--', label=r'$\text{sin}(t)$')
plt.xlabel(r'$t$', fontsize=14)
plt.ylabel(r'$\text{sin}(t)$', fontsize=14)
plt.title(r'$\text{Plot of sin(t)}$', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
