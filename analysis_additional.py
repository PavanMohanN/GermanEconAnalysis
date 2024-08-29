import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.stats import pearsonr

# Load the datasets
df1 = pd.read_csv('/content/Employement Germany Modified.csv')
df2 = pd.read_csv('/content/GDP Germany Modified.csv')
df3 = pd.read_csv('/content/Compensation Germany Modified.csv')

# Drop unnecessary columns
df1 = df1.drop('DATE', axis=1)
df2 = df2.drop('DATE', axis=1)
df3 = df3.drop('DATE', axis=1)
df3 = df3.drop('Compensation', axis=1)

# Merge datasets
merged_df = pd.merge(df1, df2, on='Financial Quarter')
merged_df = pd.merge(merged_df, df3, on='Financial Quarter')

# Residual Analysis
def compute_residuals(actual, predicted):
    return actual - predicted

# Example regression prediction (placeholder)
def simple_linear_regression(x, y):
    coefficients = np.polyfit(x, y, 1)
    predicted = np.polyval(coefficients, x)
    return predicted

# Apply to GDP vs Employment Rate
x = merged_df['GDP'].values
y = merged_df['Employement Rate'].values
predicted = simple_linear_regression(x, y)
residuals = compute_residuals(y, predicted)

# Plot residuals
plt.figure(figsize=(14, 7))
plt.plot(merged_df['Financial Quarter'], residuals, label='Residuals')
plt.xlabel('Financial Quarter')
plt.ylabel('Residuals')
plt.title('Residual Analysis: Employment Rate vs GDP')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.savefig('residuals_plot.png')
plt.show()

# Correlation Analysis
def correlation_analysis(df, col1, col2):
    correlation, _ = pearsonr(df[col1], df[col2])
    return correlation

# Example correlation
correlation_gdp_compensation = correlation_analysis(merged_df, 'GDP', 'Compensation in Billions')
print(f'Correlation between GDP and Compensation: {correlation_gdp_compensation:.2f}')

# FFT Analysis
def fft_analysis(data, title):
    N = len(data)
    T = 1.0 / 1.0  # Assuming unit time intervals
    yf = fft(data)
    xf = np.fft.fftfreq(N, T)[:N//2]

    plt.figure(figsize=(14, 7))
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.title(title)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.savefig(f'fft_{title}.png')
    plt.show()

# Apply FFT to GDP data
fft_analysis(merged_df['GDP'], 'FFT of GDP')

# Apply FFT to Compensation data
fft_analysis(merged_df['Compensation in Billions'], 'FFT of Compensation in Billions')

# Apply FFT to Employment Rate data
fft_analysis(merged_df['Employement Rate'], 'FFT of Employment Rate')
