"""
evaluate.py
Run the end-to-end radar DSP PoC and generate plots + report.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from waveform import lfm_chirp
from channel_sim import simulate_echo
from matched_filter import pulse_compress
from range_doppler import range_doppler_map
from cfar import ca_cfar_1d
from report_generator import make_report

def savefig(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()

def main():
    # Parameters (tunable)
    fs = 5e6
    pulse_width = 40e-6
    bw = 2e6
    prf = 2e3
    fc = 10e9
    n_pulses = 64

    target_range_m = 4500.0
    target_vel_mps = 30.0
    snr_db = 5.0

    # Generate waveform
    t, tx = lfm_chirp(fs, pulse_width, bw)

    # Simulate received echo matrix
    rx = simulate_echo(tx, fs, prf, fc, target_range_m, target_vel_mps, n_pulses, snr_db)

    # Pulse compression
    pc = pulse_compress(rx, tx)

    # Range profile (magnitude) for one pulse
    rp = np.abs(pc[0])

    # CFAR on range profile
    thr, det = ca_cfar_1d(rp, guard=2, train=14, pfa=1e-3)
    det_idx = np.where(det)[0]

    # Range-Doppler map
    rd = range_doppler_map(pc)
    rd_mag = 20*np.log10(np.abs(rd) + 1e-12)

    # Output paths
    base = Path(__file__).resolve().parents[1]
    plots = base/"results"/"plots"
    plots.mkdir(parents=True, exist_ok=True)

    # Plot 1: waveform
    plt.figure()
    plt.plot(t*1e6, np.real(tx))
    plt.xlabel("Time (µs)")
    plt.ylabel("Amplitude")
    plt.title("Transmit LFM waveform (real part)")
    savefig(plots/"01_waveform.png")

    # Plot 2: matched filter output range profile
    plt.figure()
    plt.plot(rp, label="|PC|")
    plt.plot(thr, label="CFAR threshold")
    plt.scatter(det_idx, rp[det_idx], marker="x", label="Detections")
    plt.xlabel("Range bin")
    plt.ylabel("Magnitude")
    plt.title("Range profile with CA-CFAR detections")
    plt.legend()
    savefig(plots/"02_range_cfar.png")

    # Plot 3: range-doppler heatmap
    plt.figure()
    plt.imshow(rd_mag, aspect='auto', origin='lower')
    plt.xlabel("Range bin")
    plt.ylabel("Doppler bin")
    plt.title("Range-Doppler Map (dB)")
    plt.colorbar(label="Magnitude (dB)")
    savefig(plots/"03_range_doppler.png")

    # Simple performance summary (simulation-based)
    summary_lines = [
        f"Sampling rate fs = {fs/1e6:.1f} MHz, bandwidth = {bw/1e6:.1f} MHz, pulse width = {pulse_width*1e6:.1f} µs",
        f"PRF = {prf:.0f} Hz, carrier = {fc/1e9:.1f} GHz, pulses = {n_pulses}",
        f"Target: range = {target_range_m:.0f} m, velocity = {target_vel_mps:.1f} m/s, SNR = {snr_db:.1f} dB (simulated)",
        f"CFAR detections (range bins): {det_idx[:10].tolist()} {'...' if det_idx.size>10 else ''}"
    ]

    report_path = base/"results"/"report.pdf"
    make_report(str(report_path),
                title="CPDS 2025 PDS 70 – Radar Signal Processor PoC (Python)",
                summary_lines=summary_lines,
                plot_paths=[str(plots/"01_waveform.png"), str(plots/"02_range_cfar.png"), str(plots/"03_range_doppler.png")])

    print("Done. Outputs:")
    print(f"- Plots: {plots}")
    print(f"- Report: {report_path}")

if __name__ == "__main__":
    main()
