"""
waveform.py
Waveform generation utilities for radar PoC.
"""
import numpy as np
from scipy.signal import chirp

def lfm_chirp(fs: float, pulse_width: float, bw: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate complex baseband LFM chirp.
    fs: sampling frequency (Hz)
    pulse_width: pulse duration (s)
    bw: bandwidth (Hz)
    Returns (t, s) where s is complex chirp.
    """
    n = int(np.round(fs * pulse_width))
    t = np.arange(n) / fs
    f0 = -bw/2
    f1 = bw/2
    real = chirp(t, f0=f0, f1=f1, t1=pulse_width, method='linear', phi=0)
    # Use analytic signal approximation for complex baseband (I + jQ)
    # Simple approach: apply quadrature by 90-degree phase shift using sin/cos
    phase = 2*np.pi*(f0*t + 0.5*(f1-f0)/pulse_width*t**2)
    s = np.exp(1j*phase)
    return t, s
