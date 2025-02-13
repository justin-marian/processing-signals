""" ex3.py """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from scipy.fft import fft2, ifft2


def rgb2gray(rgb: np.ndarray) -> np.ndarray:
    """Convert RGB image to grayscale."""
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def plot_image(imag: np.ndarray,
               title: str, cmap: str = 'gray', vmin=0, vmax=1):
    """Utility function to display images."""
    plt.figure(figsize=(6, 6))
    plt.imshow(imag, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.title(title)
    plt.axis('off')
    plt.show()


###################################################
print(f"\n1. Loading and Converting Image to Grayscale")
print(f"=======================================\n")
###################################################

image_file_path: str = "../data/peppers.png"
img: np.ndarray = image.imread(image_file_path)

plot_image(img, r"$\text{Original Image}$")

gray_img: np.ndarray = rgb2gray(img)
plot_image(gray_img, r"$\text{Grayscale Image}$")

###################################################
print(f"\n2. Computing and Visualizing 2D FFT Spectrum")
print(f"=======================================\n")
###################################################

fft_img: np.ndarray = fft2(gray_img)
plot_image(np.log(np.abs(fft_img) + 1e-10),
           r"$\text{2D FFT Spectrum}$", cmap='viridis')

###################################################
print(f"\n3. Creating Frequency Filters (High/Low Pass)")
print(f"=======================================\n")
###################################################

rows, cols = gray_img.shape
crow, ccol = rows // 2, cols // 2

fc_low: float = 0.2  # Low-frequency cutoff
corner_size_row: int = int(crow * fc_low)
corner_size_col: int = int(ccol * fc_low)

# Low-pass mask (corners)
low_freq_mask: np.ndarray = np.zeros((rows, cols), dtype=bool)
low_freq_mask[:corner_size_row, :corner_size_col] = True    # Top-left
low_freq_mask[:corner_size_row, -corner_size_col:] = True   # Top-right
low_freq_mask[-corner_size_row:, :corner_size_col] = True   # Bottom-left
low_freq_mask[-corner_size_row:, -corner_size_col:] = True  # Bottom-right

# High-pass mask (all except corners)
high_freq_mask: np.ndarray = ~low_freq_mask

###################################################
print(f"\n4. Applying Frequency Filters")
print(f"=======================================\n")
###################################################

S1: np.ndarray = fft_img * low_freq_mask   # Low-pass filter
S2: np.ndarray = fft_img * high_freq_mask  # High-pass filter

plot_image(np.log(np.abs(S2) + 1e-10),
           r"$\text{High-Pass Filtered Spectrum}$", cmap='viridis')
plot_image(np.log(np.abs(S1) + 1e-10),
           r"$\text{Low-Pass Filtered Spectrum}$", cmap='viridis')

###################################################
print(f"\n5. Reconstructing Images from Filtered Spectra")
print(f"=======================================\n")
###################################################

# High-Frequency Image
reconstructed_img_high_freq: np.ndarray = np.abs(ifft2(S2))
plot_image(reconstructed_img_high_freq,
           r"$\text{Reconstructed Image (High Frequencies)}$")

# Low-Frequency Image
reconstructed_img_low_freq: np.ndarray = np.abs(ifft2(S1))
plot_image(reconstructed_img_low_freq,
           r"$\text{Reconstructed Image (Low Frequencies)}$")

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
