# Decomposing Economic Indicators: A Study of Compensation, GDP, and Employment Rate in Germany Through Empirical Mode Decomposition
Overview
This README provides instructions and explanations for the Python and MATLAB code used for analyzing economic data through Empirical Mode Decomposition (EMD). The analysis involves processing datasets related to Employment Rate, GDP, and Compensation in Germany, performing EMD, and visualizing the results.

Files
Python Code: emd_analysis.py
MATLAB Code: analysis.m
Data Files:
/content/Employement Germany Modified.csv
/content/GDP Germany Modified.csv
/content/Compensation Germany Modified.csv
Python Code: emd_analysis.py
Description
The Python script performs the following tasks:

Data Collection and Preprocessing:

Loads data from CSV files containing Employment Rate, GDP, and Compensation information.
Drops unnecessary columns and merges the datasets on the 'Financial Quarter'.
Empirical Mode Decomposition (EMD):

Applies EMD to the GDP, Compensation, and Employment Rate data to decompose the time series into Intrinsic Mode Functions (IMFs).
Analysis and Visualization:

Plots the original signals and their IMFs for each dataset.
Saves the plots and analysis results as PNG files and CSV files for reporting purposes.
