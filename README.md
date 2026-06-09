# PDS 70 Radar Signal Processor PoC (CPDS 2025)

## Overview

This repository contains a Python-based Proof of Concept (PoC) developed for **CPDS 2025 – PDS 70: Single Module Radar and Radar Signal Processor Cards**.

The project demonstrates the fundamental radar signal processing chain, including waveform generation, target echo simulation, pulse compression, Range-Doppler processing, and target detection using CFAR techniques. It serves as a lightweight framework for evaluating radar signal processing concepts and validating detection performance in a simulated environment.

---

## Objectives

* Generate radar transmission waveforms.
* Simulate target echoes with configurable range and velocity.
* Perform pulse compression using matched filtering.
* Generate Range-Doppler maps through FFT-based processing.
* Detect targets using CA-CFAR algorithms.
* Automatically generate visualizations and performance reports.

---

## Features

### Waveform Generation

* Linear Frequency Modulated (LFM) chirp generation.
* Configurable bandwidth, pulse duration, and sampling parameters.

### Echo Simulation

* Range-delay modelling.
* Doppler frequency shift simulation.
* Support for configurable target parameters.

### Pulse Compression

* Matched filtering implementation.
* Improved range resolution through pulse compression.

### Range-Doppler Processing

* Two-dimensional FFT processing.
* Generation of Range-Doppler maps for target analysis.

### Target Detection

* Cell Averaging Constant False Alarm Rate (CA-CFAR).
* Automatic threshold estimation and target extraction.

### Automated Reporting

* Plot generation and storage.
* PDF report generation summarizing results and detections.

---

## Project Structure

```text
PDS70-Radar-Signal-Processor/
│
├── src/
│   ├── waveform.py
│   ├── simulator.py
│   ├── processing.py
│   ├── cfar.py
│   └── evaluate.py
│
├── results/
│   ├── plots/
│   └── report.pdf
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd PDS70-Radar-Signal-Processor
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Evaluation

Execute the complete radar signal processing pipeline:

```bash
python src/evaluate.py
```

The script will:

1. Generate an LFM chirp waveform.
2. Simulate radar target echoes.
3. Apply matched filtering for pulse compression.
4. Perform Range-Doppler processing.
5. Execute CA-CFAR detection.
6. Save plots and generate a PDF report.

---

## Output

### Generated Plots

Saved under:

```text
results/plots/
```

Examples include:

* Transmitted waveform
* Received echo signal
* Pulse compression output
* Range profile
* Range-Doppler map
* CFAR detection results

### Evaluation Report

Generated automatically at:

```text
results/report.pdf
```

The report contains:

* Processing parameters
* Detection results
* Performance visualizations
* Summary of observations

---

## Radar Processing Pipeline

```text
LFM Chirp Generation
          ↓
Echo Simulation
(Range + Doppler)
          ↓
Matched Filtering
(Pulse Compression)
          ↓
Range Processing
          ↓
Doppler Processing
          ↓
Range-Doppler Map
          ↓
CA-CFAR Detection
          ↓
Results & Report Generation
```

---

## Applications

* Radar signal processing education
* Defense and aerospace research
* Detection algorithm evaluation
* Range-Doppler analysis studies
* Prototype development for radar systems

---

## Future Enhancements

* Multiple target simulation
* Clutter and noise modelling
* MTI/MTD processing
* Advanced CFAR variants (GO-CFAR, SO-CFAR, OS-CFAR)
* Tracking algorithms (Kalman Filter, JPDA)
* Real-time processing support
* Hardware-in-the-loop integration

---

## License

This project is provided for educational, research, and proof-of-concept purposes.

---

## Author

Developed as part of **CPDS 2025 – PDS 70 Radar Signal Processor PoC**.
