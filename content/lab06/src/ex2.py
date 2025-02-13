""" ex2.py """

import time
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.io.wavfile import write


def play_sound(_audio: np.ndarray, _sampling_rate: int, duration: float):
    """Play audio signal."""
    print("Playing sound...")
    sd.play(_audio, _sampling_rate)
    time.sleep(duration)
    sd.stop()


def compute_fft(_signal: np.ndarray, _sampling_rate: int) -> tuple[np.ndarray, np.ndarray]:
    """The FFT and frequency axis."""
    N: int = len(_signal)
    _freqs: np.ndarray = np.fft.fftfreq(N, 1 / _sampling_rate)
    spectrum: np.ndarray = fft(_signal)
    return _freqs, spectrum  # Ensure tuple return

def plot_spectrum(_freqs: np.ndarray, spectrum: np.ndarray, title: str):
    """Plot FFT magnitude spectrum."""
    plt.figure(figsize=(12, 4))
    plt.plot(_freqs[:len(_freqs) // 2], np.abs(spectrum[:len(spectrum) // 2]))
    plt.title(title, fontsize=14)
    plt.xlabel("Frequency (Hz)", fontsize=12)
    plt.ylabel("Magnitude", fontsize=12)
    plt.grid(True)
    plt.show()


def filter_fft(_original_fft: np.ndarray, _freqs: np.ndarray, _fc: int) -> np.ndarray:
    """Low-pass filter by zeroing out frequencies beyond fc."""

    _filtered_fft: np.ndarray = np.zeros_like(_original_fft, dtype=np.complex128)

    _fc = _fc if isinstance(_fc, (tuple, list)) else _fc
    signal_indices = [int(i) for i, _f in enumerate(_freqs) if -_fc < np.real(_f) < _fc]

    _filtered_fft[signal_indices] = _original_fft[signal_indices]
    return _filtered_fft


def compute_snr(_original_fft: np.ndarray, _freqs: np.ndarray, _fc: int, _noise_range: int) -> tuple[float, float]:
    """Compute Signal-to-Noise Ratio (SNR) and return it as a tuple."""

    _fc = _fc if isinstance(_fc, (tuple, list)) else _fc
    _noise_range = _noise_range if isinstance(_noise_range, (tuple, list)) else _noise_range

    signal_indices = [int(i) for i, _f in enumerate(_freqs)
                      if -_fc < np.real(_f) < _fc]
    noise_indices = [int(i) for i, _f in enumerate(_freqs)
                     if (-_noise_range < np.real(_f) < -_fc) or (_fc < _f < _noise_range)]

    N_signal = len(signal_indices)
    N_noise = len(noise_indices)

    if N_signal == 0 or N_noise == 0:
        raise ValueError("Signal or Noise index set is empty. Adjust frequency ranges.")

    signal_power = np.sum(np.abs(_original_fft[signal_indices]) ** 2) / N_signal
    noise_power = np.sum(np.abs(_original_fft[noise_indices]) ** 2) / N_noise

    snr = signal_power / noise_power
    snr_db = 10 * np.log10(snr)

    print(f"Signal Power: {signal_power:.4f} W")
    print(f"Noise Power: {noise_power:.4f} W")
    print(f"SNR: {snr:.4f}")
    print(f"SNR (in dB): {snr_db:.4f} dB(s)")

    return snr, snr_db  # SNR and SNR in dB

def normalize_audio(audio: np.ndarray) -> np.ndarray:
    """Normalize audio for 16-bit WAV format."""
    max_val = np.max(np.abs(audio))
    return np.int16(audio / max_val * 32767)


###################################################
print(f"\n1. Loading Noisy Sound Data")
print(f"=======================================\n")
###################################################

in_file_path: str = f"../data/noisy_sound.npz"
out_file_path: str = f"../data/filtered_sound.wav"

npz = np.load(in_file_path)
noisy_sound: np.ndarray = npz['noisy_sound']
fs: int = npz['fs']               # Sampling frequency

T: float = len(noisy_sound) / fs  # Duration of sound

# Play original noisy sound
play_sound(noisy_sound, fs, T)

###################################################
print(f"\n2. Computing FFT of Noisy Sound")
print(f"=======================================\n")
###################################################

freqs, fft_result = compute_fft(noisy_sound, fs)
plot_spectrum(freqs, fft_result, r"$\text{Original FFT Magnitude}$")

###################################################
print(f"\n3. Filtering Sound (Low-pass Filter at 500 Hz)")
print(f"=======================================\n")
###################################################

fc: int = 500  # Hz - Cut-off frequency
filtered_fft = filter_fft(fft_result, freqs, fc)

# SNR before filtering
compute_snr(fft_result, freqs, fc, 4000)

plot_spectrum(freqs, filtered_fft, r"$\text{Filtered FFT Magnitude (0-500 Hz)}$")

###################################################
print(f"\n4. Inverse FFT to Reconstruct Filtered Sound")
print(f"=======================================\n")
###################################################

filtered_sound = np.real(ifft(filtered_fft))

# Normalize and save the filtered sound
filtered_sound_int16 = normalize_audio(filtered_sound)
write(out_file_path, fs, filtered_sound_int16)

###################################################
print(f"\n5. Playing Filtered Sound")
print(f"=======================================\n")
###################################################

play_sound(filtered_sound, fs, T)

###################################################
print("\nSimulation complete!")
print("=======================================\n")
###################################################
