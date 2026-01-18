"""
channel_sim.py
Simple echo channel model: range delay + Doppler + noise.
"""
import numpy as np

C = 299_792_458.0  # speed of light m/s

def simulate_echo(tx: np.ndarray, fs: float, prf: float, fc: float,
                  target_range_m: float, target_vel_mps: float,
                  n_pulses: int, snr_db: float) -> np.ndarray:
    """
    Simulate received pulses (baseband) for one point target.
    Returns rx matrix shape (n_pulses, n_samples_per_pulse)
    """
    n = tx.size
    rx = np.zeros((n_pulses, n), dtype=np.complex128)

    # Range delay (two-way)
    tau = 2 * target_range_m / C
    delay_samp = int(np.round(tau * fs))
    delay_samp = min(max(delay_samp, 0), n-1)

    # Doppler frequency (approx) for monostatic radar: fd = 2*v/lambda = 2*v*fc/c
    fd = 2 * target_vel_mps * fc / C

    # Build delayed signal
    delayed = np.zeros(n, dtype=np.complex128)
    delayed[delay_samp:] = tx[:n-delay_samp]

    # Pulse-to-pulse doppler phase progression
    for k in range(n_pulses):
        t = np.arange(n) / fs
        doppler = np.exp(1j * 2*np.pi*fd*(t + k/prf))
        rx[k, :] = delayed * doppler

    # Add noise based on SNR relative to signal power
    sig_power = np.mean(np.abs(rx)**2) + 1e-12
    snr_lin = 10**(snr_db/10)
    noise_power = sig_power / snr_lin
    noise = (np.random.randn(*rx.shape) + 1j*np.random.randn(*rx.shape)) * np.sqrt(noise_power/2)
    rx_noisy = rx + noise
    return rx_noisy
