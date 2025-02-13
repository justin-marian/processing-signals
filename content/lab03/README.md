# 🚀 [Signals in Frequency Domain](https://ocw.cs.pub.ro/courses/ps/labs_python/03)

---

## 📝 Objectives  

- **Fourier Series:** Compute and visualize Fourier coefficients for different signals.  
- **RMS Error Analysis:** Evaluate the reconstruction accuracy using **Root Mean Square (RMS) Error**.  
- **Signal Encoding:** Generate and encode digital signals using sinusoidal functions.  
- **DFT & IDFT:** Implement **Discrete Fourier Transform (DFT)** and its inverse to reconstruct signals.  
- **Visualization:** Graph time-domain signals, frequency components, and encoding schemes.  

---

## 🛠️ Key Concepts  

---

### ✅ Fourier Series Analysis  

- Computes Fourier coefficients for a rectangular signal.  
- Uses **DFT (Discrete Fourier Transform)** to analyze signal decomposition.  
- **Visualization:**  
  - Plots the original rectangular wave.  
  - Displays magnitude of Fourier coefficients.  
  - Compares reconstructed and original signals.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Amplitude of the Signal** | $A$ | The maximum magnitude of the signal, determining its peak value. |
| **Period of the Signal** | $T$ | The duration after which the signal repeats. |
| **Fourier Series Representation** | $s(t) = \sum_{k=-\infty}^{\infty} c_k e^{j \frac{2\pi k t}{T}}$ | Represents a periodic signal as a sum of exponentials with different frequencies. |
| **Fourier Coefficients Formula** | $c_k = \frac{1}{T} \int_0^T s(t) e^{-j \frac{2\pi k t}{T}} dt$ | Computes the contribution of each frequency component to the signal. |
| **Fourier Coefficients - Rectangular Wave** | $c_k = \begin{cases} \frac{2A}{j \pi k}, & k \text{ odd} \\ 0, & k \text{ even} \end{cases}$ | Shows that only odd harmonics contribute, and the coefficient magnitude decreases with $k$. |

---

### ✅ RMS Error Evaluation  

- Computes **RMS Error** between the original and reconstructed signal.  
- Evaluates error reduction by increasing **Fourier terms $ N $**.  
- **Visualization:**  
  - Plots **RMS error** in *normal*, *semi-log*, and *log-log* scale.  
  - Determines the smallest **$ N $** for reconstruction accuracy.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:--------------------------:|:---------------:|
| **Error between original and reconstructed signal** | $\epsilon_N (t) = s(t) - s_N (t)$ | Measures the difference between the actual and approximated signal. |
| **Fourier Series Approximation using $ N $ terms** | $s_N (t) = \sum\limits_{k=-N}^{N} c_k e^{j \frac{2\pi k t}{T}}$ | Uses only the first $N$ terms for signal reconstruction. |
| **RMS Error Formula** | $\text{rms} \epsilon_N = \sqrt{ 2 \sum\limits_{k=N}^{\infty} \|c_k\|^2 }$ | Represents the energy of the truncated Fourier coefficients. |
| **Error expressed using all coefficients** | $\text{rms} (\epsilon_{N-1}) = \sqrt{ \sum\limits_{k=-\infty}^{\infty} \left\| c_k \right\|^2 - \left( 2 \sum\limits_{k=1}^{N} \left\| c_k \right\|^2 + \left\| c_0 \right\|^2 \right) }$ | Analyzes how error decreases as $N$ increases. |

---

### ✅ Fourier Transform Implementation  

- Implements **DFT (Discrete Fourier Transform)** to compute frequency components.  
- Implements **IDFT (Inverse DFT)** for signal reconstruction.  
- Supports variable **$k_{\max}$** to control reconstruction quality.  

| **Concept** | **Mathematical Expression** | **Explanation** |
|:----------:|:-------------------------:|:---------------:|
| **Discrete Fourier Transform (DFT)** | $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi k n}{N}}$ | Converts a discrete-time signal into its frequency-domain representation. |
| **Frequency-domain coefficients** | $X[k]$ | Represents the amplitude and phase of frequency components. |
| **Number of samples** | $N$ | The total number of discrete points in the signal. |
| **Inverse Discrete Fourier Transform (IDFT)** | $x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j \frac{2\pi k n}{N}}$ | Reconstructs the original time-domain signal from its frequency representation. |
| **Reconstruction control** | $k_{\max}$ | Controls the quality of reconstruction by limiting frequency terms. |

---

### ✅ Signal Encoding & Transmission  

- Encodes a **random binary sequence** into a sinusoidal waveform.  
- Uses frequency mapping:  
  - **00** → **No signal**  
  - **01** → **$\sin{(2\pi f_1 t)}$**  
  - **10** → **$\sin{(2\pi f_2 t)}$**  
  - **11** → **Combination of $f_1$ and $f_2$**.  
- **Visualization:**  
  - Plots the encoded signal with time-domain analysis.  

---

## 📊 Results  

- Increasing **$k_{\max}$** improves signal reconstruction.  
- **RMS Error** decreases with more Fourier terms.  
- **Signal encoding successfully maps digital sequences to sinusoidal waves.**  
- **DFT & IDFT provide accurate spectral and time-domain representations.**  

---
