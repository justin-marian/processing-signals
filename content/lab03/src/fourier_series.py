""" fourier_series.py """

import numpy as np

def dft(
        _k_max: int,
        _amplitude: float
) -> tuple[np.ndarray, np.ndarray]:
    """Fourier coefficients for a rectangular signal."""
    print(f"Computing Fourier coefficients for k_max = {_k_max}, amplitude = {_amplitude}...")

    _k_values: np.ndarray = np.arange(-_k_max, _k_max + 1, dtype=np.int32)
    _ck: np.ndarray = np.zeros(len(_k_values), dtype=np.complex128)

    for _i in range(len(_k_values)):
        _k_value: int = int(_k_values[_i])

        if _k_value != 0 and _k_value % 2 != 0:
            _ck[_i] = 2 * _amplitude / (1j * np.pi * _k_value)
        else:
            _ck[_i] = 0

    print("Fourier coefficients computed successfully.")
    return _k_values, _ck

def idft(
        _time_samples: np.ndarray,
        _k_values: np.ndarray,
        _ck: np.ndarray,
        _period: int
) -> np.ndarray:
    """Discrete signal using the DFT."""
    print("Reconstructing signal using Fourier series...")

    _s_rec: np.ndarray = np.zeros(_period, dtype=np.complex128)

    for _i in range(len(_k_values)):
        _s_rec += _ck[_i] * np.exp(1j * 2 * np.pi * _k_values[_i] * _time_samples / _period)

    print("Signal reconstruction complete.")
    return np.real(_s_rec)

def rms_error(_ck: np.ndarray, _n_max: int) -> np.ndarray:
    """RMS error between the original and reconstructed signal."""
    total_power: float = 1.0  # Total power: A^2
    _rms_error: np.ndarray = np.zeros(_n_max)

    for _N in range(1, _n_max + 1):
        power_of_terms: float = 2 * np.sum(np.abs(_ck[1:_N + 1]) ** 2) + np.abs(_ck[0]) ** 2
        result: float = total_power - power_of_terms
        _rms_error[_N - 1] = np.sqrt(result)

    print("RMS error computed successfully.")
    return _rms_error