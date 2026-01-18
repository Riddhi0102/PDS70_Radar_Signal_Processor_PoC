"""
matched_filter.py
Matched filtering / pulse compression.
"""
import numpy as np
from scipy.signal import fftconvolve

def pulse_compress(rx: np.ndarray, tx: np.ndarray) -> np.ndarray:
    """
    Apply matched filter to each received pulse.
    rx: (n_pulses, n_samples)
    tx: (n_samples,) transmitted waveform
    Returns compressed pulses same shape.
    """
    h = np.conj(tx[::-1])
    out = np.zeros_like(rx, dtype=np.complex128)
    for k in range(rx.shape[0]):
        out[k,:] = fftconvolve(rx[k,:], h, mode='same')
    return out
