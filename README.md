# TIDI Wave Analysis

A Python-based scientific data analysis project for processing TIDI atmospheric wind observations and analyzing wave characteristics.

This project refactors part of my previous scientific data analysis workflow into a modular and reproducible Python pipeline.

## 1. Project Overview

The project processes TIDI wind observation data and performs wave-number / period analysis on zonal wind observations.

The current pipeline includes:

- TIDI data loading
- Data quality control
- Altitude and latitude selection
- Time and longitude coordinate processing
- Harmonic fitting
- Wave-number / period scanning
- Amplitude spectrum visualization

## 2. Analysis Pipeline

```text
Raw TIDI Data
      |
      v
Data Loading
      |
      v
Data Cleaning
      |
      v
Altitude / Latitude Selection
      |
      v
Coordinate Processing
      |
      v
Wave-number / Period Scan
      |
      v
Harmonic Fitting
      |
      v
Amplitude Spectrum
      |
      v
Visualization
```

## 3. Project Structure

```text
WeatherProject/
├── raw/
│   └── ...
├── outputs/
│   └── result.png
├── config.py
├── data_read.py
├── data_clean.py
├── data_select.py
├── data_process.py
├── data_fit.py
├── painting.py
├── wave_period_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Main Modules

- `data_read.py`: loads and combines raw TIDI data.
- `data_clean.py`: performs data quality control and removes invalid observations.
- `data_select.py`: selects observations by altitude and latitude.
- `data_process.py`: processes coordinates for subsequent analysis.
- `data_fit.py`: performs harmonic fitting and scans wave-number / period combinations.
- `painting.py`: generates the final spectrum visualization.
- `wave_period_main.py`: main entry point of the analysis pipeline.

## 4. Method

For a given wave number and period, the zonal wind is modeled using harmonic components:

\[
u = A\cos(\theta) + B\sin(\theta) + C
\]

where the phase \(\theta\) depends on time, longitude, period, and wave number.

The corresponding wave amplitude is calculated as:

\[
R = \sqrt{A^2 + B^2}
\]

The program scans different wave-number and period combinations and visualizes the fitted amplitude distribution.

## 5. Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd WeatherProject
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Usage

Place the required TIDI data files in the configured data directory.

Run:

```bash
python wave_period_main.py
```

The generated figure will be saved to:

```text
outputs/
```

## 7. Example Result

![Wave-period spectrum](outputs/result.png)

Briefly describe the result here after final verification.

For example:

- dominant wave number: [fill after verification]
- dominant period: [fill after verification]
- maximum fitted amplitude: [fill after verification]

## 8. Data Processing Assumptions

Document important analysis assumptions here.

Examples:

- Selected altitude: 95
- Selected latitude range: all
- Quality-control criteria: data_ok = T, |u|<=300...
- Measurement track selection:refer from other paper 'C'
- Longitude representation: radians
- Time representation: elapsed hours from the analysis start

These assumptions should match the implementation.

## 9. Validation

The harmonic fitting implementation can be checked using synthetic data with known coefficients.

For example, if:

```text
A = 20
B = 10
```

the expected amplitude is:

```text
sqrt(20^2 + 10^2) ≈ 22.36
```

The fitted result should be close to the theoretical value.

## 10. Limitations and Future Work

The current version focuses on wave-number / period analysis.

Possible future extensions include:

- Latitude-altitude wave amplitude analysis
- Time-period evolution analysis
- More systematic quality-control procedures
- Cross-year data processing

These features are outside the scope of the current version.

## 11. Tech Stack

- Python
- NumPy
- xarray
- SciPy
- Matplotlib
- Git

## 12. Project Purpose

The project is primarily an engineering reconstruction of a scientific data analysis workflow.

Its main goals are to practice:

- processing real scientific datasets;
- modular Python development;
- numerical analysis;
- reproducible analysis pipelines;
- debugging and validation;
- Git-based project management.


