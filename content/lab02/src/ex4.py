""" ex4.py """

import numpy as np
import matplotlib.pyplot as plt

###################################################
print(f"\n1. Defining System Functions")
print(f"=======================================\n")
###################################################

def system_control(y_prev: int, err: int) -> int:  # S1
    """System Transfer Function updates current speed based on error."""
    if err > 10:
        return y_prev + 5
    elif err > 0:
        return y_prev + 1
    else:  # e == 0
        return y_prev

def system_feedback(y_prev: int) -> int:  # S2
    """System Feedback Function returns the measured speed."""
    return y_prev

###################################################
print(f"\n2. Initializing System Parameters")
print(f"=======================================\n")
###################################################

N: int = 20                 # Number of iterations
r = np.full(N, 60)          # Desired speed (reference) is constant at 60 km/h
y = np.zeros(N, dtype=int)  # Output feedback sequence (initially zero)
y[0] = 7                    # Initial speed of the car is 7 km/h
e = np.zeros(N, dtype=int)  # Error sequence: e = r - y

print(f"Reference speed: {r[0]} km/h for {N} iterations.")
print(f"Initial speed: {y[0]} km/h")

###################################################
print(f"\n3. Running Feedback System Simulation")
print(f"=======================================\n")
###################################################

for i in range(N - 1):
    # Current error
    e[i] = r[i] - y[i]
    # Update speed based on error
    y[i + 1] = system_control(
        system_feedback(np.int32(y[i])),
        np.int32(e[i])
    )
    print(f"Step {i+1}: e[{i}] = {e[i]}, y[{i+1}] = {y[i+1]}")

e[-1] = r[-1] - y[-1]  # Last error value

print(f"\nFinal speed values over iterations:")
print(y)

###################################################
print(f"\n4. Plotting Speed and Error Evolution")
print(f"=======================================\n")
###################################################

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(y, marker='o', linestyle='-', color='b', linewidth=3, markersize=6, markerfacecolor='red')
plt.title(r'Speed of Car with Feedback System', fontsize=16)
plt.xlabel(r'Step', fontsize=14)
plt.ylabel(r'Speed (km/h)', fontsize=14)
plt.axhline(y=r[0], color='green', linestyle='--', linewidth=2, label=r'Desired Speed $r=60$ km/h')
plt.grid(True, which='both', linestyle='--', linewidth=1)
plt.legend(fontsize=12)

plt.subplot(2, 1, 2)
plt.plot(e, marker='s', linestyle='-', color='r', linewidth=3, markersize=6, markerfacecolor='blue')
plt.title(r'Error Improvement Over Time', fontsize=16)
plt.xlabel(r'Step', fontsize=14)
plt.ylabel(r'Error (km/h)', fontsize=14)
plt.axhline(0, linewidth=2, color='black', linestyle='--', label='Zero Error')
plt.grid(True, which='both', linestyle='--', linewidth=1)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
