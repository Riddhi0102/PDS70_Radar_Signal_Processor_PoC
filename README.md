# PDS 70 Radar Signal Processor PoC (CPDS 2025)

This repository contains a Python-based proof-of-concept for **CPDS 2025 – PDS 70 (Single Module Radar and Radar Signal Processor Cards)**.

## Features
- Waveform generation (LFM chirp)
- Echo simulation (range delay + Doppler)
- Matched filtering / pulse compression
- Range-Doppler processing (2D FFT)
- CA-CFAR detection (simple)
- Auto-saving plots and a PDF results report

## How to run
1) Install requirements:
```bash
pip install -r requirements.txt
```

2) Run evaluation:
```bash
python src/evaluate.py
```

Outputs:
- Plots saved to `results/plots/`
- Results report saved to `results/report.pdf`
