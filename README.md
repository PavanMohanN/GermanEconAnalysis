![Picture1](https://github.com/user-attachments/assets/7fc42212-6903-41ac-996b-895e09653c2a)

## Overview

This repository contains code for performing Empirical Mode Decomposition (EMD) on economic datasets related to Germany. The analysis involves three main datasets (provided in the repo):
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

<img src="https://github.com/user-attachments/assets/d0bbce8c-7812-4a52-9f70-2cc44e779d00" alt="Image Description" width="100" />

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

## Python Script: `analysis_additional.py`

This script will:
1. Load and preprocess the data
2. Compute and analyze residuals
3. Perform correlation analysis
4. Apply Fast Fourier Transform (FFT)
5. Visualize results
   
### Explanation

Loading and Preprocessing: The script reads the datasets and performs the necessary preprocessing steps.

### Residual Analysis:

1. compute_residuals() function calculates residuals by subtracting predicted values from actual values.
2. simple_linear_regression() is a placeholder function for linear regression (replace it with your actual regression model).
3. Plots the residuals for Employment Rate vs GDP.

### Correlation Analysis:

correlation_analysis() computes Pearson correlation coefficients between two specified columns.

### FFT Analysis:

fft_analysis() function performs Fast Fourier Transform on the given data and plots the frequency domain representation.

### Usage

Save the script as analysis_additional.py.

Ensure you have the required libraries (pandas, numpy, matplotlib, scipy).

### Run the script:
  ```sh
python analysis_additional.py
  ```
This script provides a comprehensive analysis including residuals, correlation, and FFT, which complements the previous EMD analysis.

<img src="https://github.com/user-attachments/assets/17f51656-0151-4819-b111-879b180c8d94" alt="Image Description" width="100" />

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

`Created in Aug 2024`

`@author: Pavan Mohan Neelamraju`

`Affiliation: Indian Institute of Technology Madras`

**Email**: npavanmohan3@gmail.com

**Personal Website 🔴🔵**: [[pavanmohan.netlify.app](https://pavanmohan.netlify.app/)]
