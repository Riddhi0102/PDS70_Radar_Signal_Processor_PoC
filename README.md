# PDS 70 Radar Signal Processor PoC (CPDS 2025)

## Overview

This repository contains a Python-based Proof of Concept (PoC) developed for **CPDS 2025 – PDS 70**.

The project implements a simplified radar digital signal processing (DSP) chain, demonstrating key radar processing stages including waveform generation, echo simulation, pulse compression, Range-Doppler processing, and target detection using CA-CFAR.

The implementation simulates a single moving target and generates plots and a PDF report to visualize processing results.

---

## Features

* Complex baseband LFM (Linear Frequency Modulated) chirp generation
* Single-target echo simulation
* Range delay modelling based on target distance
* Doppler shift simulation based on target velocity
* Additive White Gaussian Noise (AWGN) channel model
* Pulse compression using matched filtering
* Range-Doppler processing using 2D FFT
* 1D Cell Averaging CFAR (CA-CFAR) detection
* Automatic plot generation
* PDF report generation

---

## Radar Processing Chain

```text
LFM Chirp Generation
          │
          ▼
Echo Simulation
(Range Delay + Doppler + Noise)
          │
          ▼
Matched Filtering
(Pulse Compression)
          │
          ▼
Range Profile Generation
          │
          ▼
CA-CFAR Detection
          │
          ▼
Range-Doppler Processing
(2D FFT)
          │
          ▼
Plots & PDF Report
```

---

## Project Structure

```text
PDS70-Radar-Signal-Processor/
│
├── waveform.py              # LFM waveform generation
├── channel_sim.py           # Echo simulation
├── matched_filter.py        # Pulse compression
├── range_doppler.py         # Range-Doppler processing
├── cfar.py                  # CA-CFAR detection
├── report_generator.py      # PDF report generation
├── evaluate.py              # End-to-end evaluation pipeline
├── requirements.txt
│
├── results/
│   ├── plots/
│   └── report.pdf
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd PDS70-Radar-Signal-Processor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the complete radar DSP pipeline:

```bash
python evaluate.py
```

The script performs:

1. LFM waveform generation
2. Echo simulation
3. Pulse compression
4. Range profile generation
5. CA-CFAR detection
6. Range-Doppler processing
7. Plot generation
8. PDF report creation

---

## Simulation Parameters

Default simulation parameters:

| Parameter         | Value  |
| ----------------- | ------ |
| Sampling Rate     | 5 MHz  |
| Pulse Width       | 40 µs  |
| Bandwidth         | 2 MHz  |
| PRF               | 2 kHz  |
| Carrier Frequency | 10 GHz |
| Number of Pulses  | 64     |
| Target Range      | 4500 m |
| Target Velocity   | 30 m/s |
| SNR               | 5 dB   |

These values can be modified directly in `evaluate.py`.

---

## Outputs

### Generated Plots

Saved in:

```text
results/plots/
```

Generated visualizations include:

* Transmit LFM waveform
* Range profile with CA-CFAR detections
* Range-Doppler map

### PDF Report

Generated automatically at:

```text
results/report.pdf
```

The report contains:

* Simulation parameters
* Processing summary
* Generated plots
* Detection results

---

## Example Processing Flow

```text
Target Parameters
        │
        ▼
Echo Simulation
        │
        ▼
Pulse Compression
        │
        ▼
Range Detection (CFAR)
        │
        ▼
Range-Doppler Analysis
        │
        ▼
Result Visualization
```

---

## Applications

* Radar signal processing education
* DSP algorithm prototyping
* Radar detection studies
* Range-Doppler analysis demonstrations
* CPDS 2025 project evaluation

---

## Future Enhancements

* Multiple target simulation
* Clutter modelling
* Advanced CFAR algorithms
* Target tracking algorithms
* MIMO radar support
* Real-time data processing
* Hardware integration

---

## License

This project is intended for educational, research, and proof-of-concept purposes.

---

## Author

Developed for **CPDS 2025 – PDS 70 Radar Signal Processor Proof of Concept**.
