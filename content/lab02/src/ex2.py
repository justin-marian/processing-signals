""" ex2.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Signal Generation")
print(f"=======================================\n")
###################################################

def ramp(n: int) -> np.ndarray:
    """Generates a ramp signal: r(i)"""
    return np.array([t for t in range(n)])

def ustep(n: int) -> np.ndarray:
    """Generates a unit step signal: u(i)"""
    return np.ones(n, dtype=int)

N: int = 200  # Number of points
T: int = 100  # Period

print(f"Generating signals with N = {N} points and delay T = {T}...")

# Sequence of input data
x: np.ndarray = np.arange(0, N)

###################################################
print(f"\n2. Generating Base Signals")
print(f"=======================================\n")
###################################################

print("Generating ramp and unit step signals...")

s1: np.ndarray = ramp(N)                                        # r(i)
s2: np.ndarray = -np.pad(ramp(N)[:N-T], (T, 0))       # r(i-T)
s3: np.ndarray = -T * np.pad(ustep(N)[:N-T], (T, 0))  # T * u(i-T)

print("Base signals generated successfully.")

###################################################
print(f"\n3. Combining Signals")
print(f"=======================================\n")
###################################################

print("Combining signals into final output...")
s: np.ndarray = s1 + s2 + s3
print("Final signal computed.")

###################################################
print(f"\n4. Plotting Signals")
print(f"=======================================\n")
###################################################

print("Plotting individual and combined signals...")

plt.figure(figsize=(10, 12))

plt.subplot(5, 1, 1)
plt.plot(x, s1, 'g-', linewidth=2)
plt.title(r'Signal ramp $\text{r(i)}$', fontsize=14)
plt.legend([r'$\text{no delay}$'], fontsize=12)
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(x, s2, 'b-', linewidth=2)
plt.title(r'Signal ramp with delay $\text{r(i-T)}$', fontsize=14)
plt.legend([r'$\text{delay r(i-T)}$'], fontsize=12)
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(x, s3, 'r-', linewidth=2)
plt.title(r'Signal unit step with delay $\text{T} \cdot \text{u(i-T)}$', fontsize=14)
plt.legend([r'$\text{delay -T} \cdot \text{u(i-T)}$'], fontsize=12)
plt.grid(True)

plt.subplot(5, 1, 4)
plt.plot(x, s, 'k-', linewidth=3)
plt.title(r'Combination of all 3 signals', fontsize=14)
plt.legend([r'$\text{final result}$'], fontsize=12)
plt.grid(True)

plt.subplot(5, 1, 5)
plt.plot(x, s1, 'g-', linewidth=3, label=r'$\text{r(i)}$')
plt.plot(x, s2, 'b-', linewidth=3, label=r'$\text{r(i-T)}$')
plt.plot(x, s3, 'r-', linewidth=3, label=r'$\text{T} \cdot \text{u(i-T)}$')
plt.plot(x, s, 'k-', linewidth=3, label=r'$\text{final result}$')
plt.title(r'All signals combined in one plot', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

plt.tight_layout()
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
