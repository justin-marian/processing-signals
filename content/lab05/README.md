# 🚀 [Digital signals - simple processing, sampling and amplitude modulation](https://ocw.cs.pub.ro/courses/ps/labs_python/05)

---

## 📝 Objectives  

- **Fourier Series:** Compute and visualize Fourier coefficients for different signals.  
- **DFT & IDFT:** Implement **Discrete Fourier Transform (DFT)** and its inverse to reconstruct signals.  
- **Amplitude Modulation:** Apply modulation techniques and analyze the effect on frequency components.  
- **Signal Filtering:** Use moving average and linear filters to smooth noisy signals.  
- **Visualization:** Plot time-domain signals, frequency spectrums, and reconstruction results.  

---

## 🛠️ Key Concepts  

---

### ✅ Signal Filtering  

- Applies a **moving average filter** to remove noise.  
- Uses **scipy's lfilter()** for linear filtering.  
- **Visualization:**  
  - Compares raw and filtered signals.  
  - Demonstrates filtering effects on noisy sinusoids.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Moving Average Filter** |$y(n) = \frac{1}{M} \sum_{i=0}^{M-1} x(n-i)$| Computes the average of the last$M$samples to smooth the signal. |

- **Steps to Implement:**
  - Generate sinusoidal signals with different frequencies (`1`, `2`, `10`, `20`, `100` Hz).
  - Apply the moving average filter on the generated signals.
  - Visualize the effect by plotting input and output sequences.
  - Analyze how the filter affects high-frequency signals.

---

### ✅ Fourier Series Analysis  

- Computes Fourier coefficients for a rectangular signal.  
- Uses **DFT (Discrete Fourier Transform)** to analyze signal decomposition.  
- **Visualization:**  
  - Plots the original rectangular wave.  
  - Displays the magnitude of Fourier coefficients.  
  - Compares reconstructed and original signals.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Fourier Series Representation** |$s(t) = \sum_{k=-\infty}^{\infty} c_k e^{j \frac{2\pi k t}{T}}$| Represents a periodic signal as a sum of exponentials with different frequencies. |
| **Fourier Coefficients Formula** |$c_k = \frac{1}{T} \int_0^T s(t) e^{-j \frac{2\pi k t}{T}} dt$| Computes the contribution of each frequency component to the signal. |

---

### ✅ Discrete Fourier Transform (DFT)  

- Implements **DFT** and **Inverse DFT (IDFT)** from scratch.  
- Uses **FFT (Fast Fourier Transform)** for efficient computation.  
- **Visualization:**  
  - Plots DFT magnitude spectrum.  
  - Compares DFT and FFT results.  
  - Demonstrates spectral shifting techniques.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Discrete Fourier Transform (DFT)** |$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi k n}{N}}$| Converts a discrete-time signal into its frequency-domain representation. |
| **Inverse Discrete Fourier Transform (IDFT)** |$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j \frac{2\pi k n}{N}}$| Reconstructs the original time-domain signal from its frequency representation. |

---

### ✅ Amplitude Modulation  

- Generates an exponentially decaying signal.  
- Modulates it with a **cosine carrier** for AM transmission.  
- **Visualization:**  
  - Displays the modulated waveform.  
  - Shows the effect of modulation on Fourier coefficients.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Exponential Decay Signal** |$s(t) = e^{-a t} u(t)$| Models a decaying signal where$a > 0$controls decay rate, and$u(t)$is the unit step function. |
| **Fourier Transform of Signal** |$S(k) = \sum_{n=0}^{N-1} s(n) e^{-j \frac{2\pi nk}{K}}$| Computes the frequency representation of$s(t)$using DFT. |
| **Amplitude Modulation** |$x(t) = (1 + s(t)) \cdot \cos(2\pi f_c t)$| Modulates the signal by multiplying it with a cosine carrier of frequency$f_c$. |

---

## 📊 Results  

- Increasing Fourier coefficients improves reconstruction accuracy.  
- DFT effectively decomposes signals into frequency components.  
- Amplitude Modulation shifts frequency content as expected.  
- Filtering techniques smooth noisy signals for better analysis.  

---
