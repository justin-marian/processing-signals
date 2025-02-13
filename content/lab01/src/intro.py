""" intro.py """

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

###################################################
print(f"\n1. Workspace script editing, console...")
print(f"=======================================\n")
###################################################

a: int = 2
b: int = 3
c: int = a + b
print(f"Performing basic arithmetic operations:")
print(f"a + b = {c}")
print("{} + {} = {}".format(a, b, a + b))
print(f"a * b = {a} * {b} = {a * b}")
print(f"a ^ b = {a} ** {b} = {a ** b}")

###################################################
print(f"\n2. Vectors")
print(f"=======================================\n")
###################################################

print(f"Creating vector arrays...")
vec: np.ndarray = np.array([1, 2, 3, 4], dtype=np.int32)
print("Vector:", vec)

vec1: np.ndarray = np.ones(7, dtype=np.int32) * 3
print("Vector with 7 elements, each = 3:", vec1)

vec2: np.ndarray = np.random.random(size=5)
print("Randomly generated vector:", vec2)

print("Accessing vector elements:")
print("First element:", vec1[0])
print("Second and third elements:", vec1[1:3])
print("Last two elements:", vec1[-2:])

###################################################
print(f"\n3. Matrices")
print(f"=======================================\n")
###################################################

print("Generating random 5x4 matrix...")
mat1: np.ndarray = np.random.random((5, 4))
print(mat1)

print("Generating 5x4 matrix filled with ones...")
mat2: np.ndarray = np.ones((5, 4))
print(mat2)

print("Summing matrices...")
mat_sum: np.ndarray = mat1 + mat2
print(mat_sum)

###################################################
print(f"\n4. Transpose")
print(f"=======================================\n")
###################################################

print("Transposing matrix...")
mat_transposed: np.ndarray = np.transpose(mat1)
print(mat_transposed)

print("Creating column vector and transposing it...")
vec_col: np.ndarray = np.ones((5, 1))
print("Column vector:\n", vec_col)

vec_col_transposed: np.ndarray = np.transpose(vec_col)
print("Transposed column vector:\n", vec_col_transposed)

###################################################
print(f"\n5. Matrices and Vectors (others)")
print(f"=======================================\n")
###################################################

print("Creating sequences and checking properties...")

v: list[int] = [int(x) for x in range(5, 15)]
print("Continuous sequence from 5 to 15:", v)

v: list[int] = [int(x) for x in range(1, 10, 3)]
print("Arithmetic progression:", v)

v: np.ndarray = np.linspace(0, 1, 5).astype(np.float32)
print("Five equally spaced elements between 0 and 1:", v)

print(f"Vector length: {len(v)}")

mat: np.ndarray = np.random.random((3, 4))
print(f"Matrix shape (dimensions): {mat.shape}")

###################################################
print(f"\n6. Strings manipulation")
print(f"=======================================\n")
###################################################

s: str = f'Signal Processing'
print("Created string:", s)

s2: str = f'Lab of ' + s
print("Concatenated string:", s2)

n: int = 7
s3: str = f'The chosen number is {n}'
print(s3)

###################################################
print(f"\n7. Plots")
print(f"=======================================\n")
###################################################

print("Plotting sinus function over the range [0, 10]...")
x: np.ndarray = np.linspace(0, 10, 100)
y: np.ndarray = np.sin(x)

plt.plot(x, y)
plt.title(r'$\sin(x)$ Function', fontsize=16)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$\sin(x)$', fontsize=14)
plt.grid(True)
plt.show()

f1: int = 1  # Hz
f2: int = 2  # Hz
t: np.ndarray = np.linspace(0, 1, 100)

sin_wave_1hz: np.ndarray = np.sin(2 * np.pi * f1 * t)
sin_wave_2hz: np.ndarray = np.sin(2 * np.pi * f2 * t)

print("Plotting sinusoid of 1 Hz...")
plt.plot(t, sin_wave_1hz, color='blue', linestyle='-')
plt.title(r'$\sin(2\pi \times 1 \times t)$ - 1 Hz', fontsize=14)
plt.grid(True)
plt.show()

print("Plotting sinusoid of 2 Hz...")
plt.plot(t, sin_wave_2hz, color='blue', linestyle='-')
plt.title(r'$\sin(2\pi \times 1 \times t)$ - 2 Hz', fontsize=14)
plt.grid(True)
plt.show()

###################################################
print(f"\n8. Signal processing")
print(f"=======================================\n")
###################################################

print("Summing two sine waves of 1 Hz and 2 Hz...")
sum_sin_waves: np.ndarray = sin_wave_1hz + np.sin(2 * np.pi * f2 * t)

plt.plot(t, sin_wave_1hz, color='blue', linestyle='-')
plt.plot(t, sum_sin_waves, color='purple', linestyle='-.')
plt.title('Sum of Two Sinusoids', fontsize=14)
plt.grid(True)
plt.show()

###################################################
print(f"\n9. Image processing")
print(f"=======================================\n")
###################################################

print("Loading images (IR, R1, R2)...")

IR: np.ndarray = mpimg.imread('../data/IR.png')
R1: np.ndarray = mpimg.imread('../data/R1.png')
R2: np.ndarray = mpimg.imread('../data/R2.png')

print("Displaying noisy image...")
plt.figure()
plt.imshow(IR)
plt.title(r'$\text{IR (Noisy Image)}$', fontsize=12)
plt.show()

print("Reconstructing original image...")
Img_initial: np.ndarray = (IR - 0.3 * (R1 + R2)) / 0.3
Img_initial = np.clip(Img_initial, 0, 1)

plt.figure(figsize=(5, 5))
plt.imshow(Img_initial)
plt.title(r'$\text{Reconstructed Image}$', fontsize=12)
plt.show()

###################################################
print(f"\n10. Row-major vs Column-major Performance")
print(f"=======================================\n")
###################################################

N: int = 1000
A: np.ndarray = np.random.rand(N, N)
B: np.ndarray = np.random.rand(N, N)
C: np.ndarray = np.zeros((N, N))

def measure_execution_time(operation_name: str, func):
    print(f"Measuring {operation_name}...")
    start_time = time.time()
    func()
    elapsed_time = time.time() - start_time
    print(f"Time {operation_name}: {elapsed_time:.6f} s")
    return elapsed_time

def row_major_traversal():
    for i in range(N):
        for j in range(N):
            C[i, j] = A[i, j] * B[i, j]

def column_major_traversal():
    for j in range(N):
        for i in range(N):
            C[i, j] = A[i, j] * B[i, j]

# Measure execution times
time_row = measure_execution_time("row-major traversal", row_major_traversal)
time_column = measure_execution_time("column-major traversal", column_major_traversal)
# Measure direct matrix operation
time_matrix_operation = measure_execution_time("direct matrix operation", lambda: A * B)

print(f"\nFinal Results:")
print(f"Time row-major: {time_row:.6f} s")
print(f"Time column-major: {time_column:.6f} s")
print(f"Time matrix operation: {time_matrix_operation:.6f} s")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
