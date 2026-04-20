# Sensor Analysis Plot Generator

This project generates synthetic temperature data for two sensors and saves a single three-panel analysis figure.

## Installation

Activate your `ece105` conda environment, then install dependencies with either `conda` or `mamba`:

```powershell
conda activate ece105
conda install numpy matplotlib
```

Or:

```powershell
conda activate ece105
mamba install numpy matplotlib
```

## Usage

Run the script from this repository directory:

```powershell
python generate_plots.py
```

## Example output

The script creates a 1x3 figure containing:
1. A scatter plot of Sensor A and Sensor B temperatures versus time.
2. Overlaid histograms of both sensors' temperature distributions with dashed mean lines.
3. A side-by-side box plot comparison with a dashed overall-mean reference line.

## Output files

Running `generate_plots.py` produces:
1. `sensor_analysis.png` — the saved analysis figure (150 DPI, tight bounding box), written to the current working directory.

## AI tools used and disclosure

[Placeholder: Describe any AI tools used, what assistance they provided, and what you reviewed or edited manually before submission.]
