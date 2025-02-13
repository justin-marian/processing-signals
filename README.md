# ˒﹚) [Signal Processing](https://ocw.cs.pub.ro/courses/ps)

---

## 📌 Signal Processing (SP) Labs  

This repository contains structured **Signal Processing (SP) labs**:
The labs focus on key concepts such as:  

- **Fourier Analysis:** Understanding frequency-domain representations of signals.  
- **DFT / FFT:** Computing and visualizing the **Discrete Fourier Transform (DFT)** and **Fast Fourier Transform (FFT)**.  
- **Signal Filtering:** Implementing **low-pass, high-pass, band-pass FIR & IIR filters** to remove noise and extract useful components from the original signal.  
- **Convolution:** Applying convolution in **time-domain and frequency-domain** for system analysis and filtering.  
- **Windowing Methods:** Reducing spectral leakage using **Hanning, Hamming, Blackman** windows.  
- **Modulation Techniques:** Understanding and implementing **Amplitude Modulation (AM), Frequency Modulation (FM), and Phase Modulation (PM)** for communication systems.  
- **Spectral Leakage & Zero-Padding:** Investigating how **signal truncation** affects frequency domain analysis and how **zero-padding** improves resolution.  
- **FM Signal Processing with RTL-SDR:** Capturing, demodulating, and analyzing **real-world FM signals** using **Software Defined Radio (SDR)** techniques.  
- **Time & Frequency Shifting:** Learning how signals transform when shifted in **time and phase**.  
- **Digital Filtering in Python:** Designing **Butterworth, Chebyshev, and Kaiser filters** using **SciPy**.  

---

## 🗂️ Labs Structure

🟢 **Python scripts** for implementation  
🟢 **Datasets & signals** for testing and processing  
🟢 **Images & plots** for visualization  
🟢 **Lecture slides & PDFs** for theoretical background  

### 📜 Lab List  

| #  | **Lab Name** | **Topics** | **Outputs** |
|----|-------------|-----------|------------|
| 1️⃣  | [Introduction to Python](https://ocw.cs.pub.ro/courses/ps/labs_python/01) | Python basics, NumPy, Matplotlib, SciPy | Signal visualizations, array operations |
| 2️⃣  | [Signals and Base Systems](https://ocw.cs.pub.ro/courses/ps/labs_python/02) | Discrete-time signals, system properties | Time-domain plots, transformations |
| 3️⃣  | [Signals in Frequency Domain](https://ocw.cs.pub.ro/courses/ps/labs_python/03) | Fourier Transform (DFT/FFT), spectral representation | Fourier spectra, magnitude-phase plots |
| 4️⃣  | [Phase/Time Shifting and Filtering](https://ocw.cs.pub.ro/courses/ps/labs_python/04) | Phase shifts, convolution properties | Shifted signals, convolution results |
| 5️⃣  | [Fourier Analysis, Filtering, Modulation](https://ocw.cs.pub.ro/courses/ps/labs_python/06) | Fourier series, filtering, modulation | Spectrograms, modulated signals |
| 6️⃣  | [DFT in Detail: Leakage, Zero-Padding](https://ocw.cs.pub.ro/courses/ps/labs_python/07) | DFT leakage, zero-padding, windowing | Frequency domain plots, leakage effects |
| 7️⃣  | [FM Signal Processing with RTL-SDR](https://ocw.cs.pub.ro/courses/ps/labs/08) | RTL-SDR, FM demodulation, signal filtering | FM spectrograms, demodulated audio |
| 8️⃣  | [Convolution, FIR Filters, Windowing](https://ocw.cs.pub.ro/courses/ps/labs_python/09) | Convolution, FIR filters, Blackman window | Filtered signals, convolution results |
| 9️⃣  | [Bandpass & Highpass FIR, IIR Filters](https://ocw.cs.pub.ro/courses/ps/labs_python/10) | FIR/IIR filter design, Butterworth, Chebyshev | Frequency response plots, filtered waveforms |

---

## ❓ How to Run  

### 🔎 Example: Running `lab06`

In `lab06`, we analyze:

- the **effects of spectral leakage** in the Discrete Fourier Transform (DFT)
- experiment with **zero-padding** to improve frequency resolution.  

🔹 **Exercise 2 - DFT Leakage and Windowing**  

**Objective:**

- Load a signal containing two sinusoidal components.  
- Compute and plot the Fourier Transform.  
- Apply **Hanning windowing** to reduce spectral leakage.  
- Compare the results before and after applying the window function.  

🔹 **Running the Python Script:**  

1️⃣ Navigate to the `src/` directory of `lab06`:  

```bash
cd lab06/src
python ex2.py
```

---
