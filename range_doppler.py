"""
range_doppler.py
Range-Doppler processing.
"""
import numpy as np
from scipy.fft import fft, fftshift

def range_doppler_map(pc: np.ndarray, nfft_range: int | None=None, nfft_doppler: int | None=None) -> np.ndarray:
    """
    pc: pulse-compressed data (n_pulses, n_samples)
    Returns RD map (n_pulses_fft, n_range_bins) after doppler FFT.
    """
    n_pulses, n_samples = pc.shape
    if nfft_range is None:
        nfft_range = int(2**np.ceil(np.log2(n_samples)))
    if nfft_doppler is None:
        nfft_doppler = int(2**np.ceil(np.log2(n_pulses)))

    # Range FFT (optional) - since matched filter already gives range profile, we can keep samples as bins.
    range_bins = pc

    # Doppler FFT across pulses
    dop = fftshift(fft(range_bins, n=nfft_doppler, axis=0), axes=0)
    return dop
