# Decomposing Economic Indicators: A Study of Compensation, GDP, and Employment Rate in Germany Through Empirical Mode Decomposition

## Overview

This repository contains code for performing Empirical Mode Decomposition (EMD) on economic datasets related to Germany. The analysis involves three main datasets:
- Employment Rate
- GDP
- Compensation in Billions

The provided Python and MATLAB scripts will help in performing EMD, analyzing Intrinsic Mode Functions (IMFs), and visualizing the results.

## Files

- **Python Code**: `emd_analysis.py`
- **MATLAB Code**: `analysis.m`
- **Data Files**:
  - `Employement Germany Modified.csv`
  - `GDP Germany Modified.csv`
  - `Compensation Germany Modified.csv`

## Python Code: `emd_analysis.py`

### Description
This script performs the following tasks:
1. **Data Collection and Preprocessing**: 
   - Loads and preprocesses datasets by dropping unnecessary columns and merging them on the 'Financial Quarter'.
2. **Empirical Mode Decomposition (EMD)**: 
   - Applies EMD to the GDP, Compensation, and Employment Rate data to decompose the time series into Intrinsic Mode Functions (IMFs).
3. **Analysis and Visualization**:
   - Plots the original signals and their IMFs for each dataset. 
   - Saves the plots as PNG files and the results as CSV files.

### Requirements
- Python 3.x
- Libraries: `pandas`, `matplotlib`, `PyEMD`
- Install libraries using pip:
  ```sh
  pip install pandas matplotlib EMD-signal
  ```

### Usage
1. Ensure all dependencies are installed.
2. Update file paths if necessary.
3. Run the script:
   ```sh
   python emd_analysis.py
   ```

## MATLAB Code: `analysis.m`

### Description
This MATLAB script performs similar tasks to the Python code:
1. **Data Collection and Preprocessing**:
   - Loads data, drops unnecessary columns, and merges datasets.
2. **Empirical Mode Decomposition (EMD)**:
   - Applies EMD to the GDP, Compensation, and Employment Rate data.
3. **Analysis and Visualization**:
   - Plots the original signals and their IMFs.

### Requirements
- MATLAB with EMD Toolbox or equivalent.
- Ensure that the EMD toolbox is added to the MATLAB path.

### Usage
1. Ensure the EMD toolbox is included in your MATLAB path.
2. Update file paths if necessary.
3. Run the script in MATLAB.
