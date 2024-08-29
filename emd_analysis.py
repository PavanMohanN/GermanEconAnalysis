import pandas as pd

# Load the datasets
df1 = pd.read_csv('/content/Employement Germany Modified.csv')  # Replace with your actual file path
df2 = pd.read_csv('/content/GDP Germany Modified.csv')          # Replace with your actual file path
df3 = pd.read_csv('/content/Compensation Germany Modified.csv')

# Drop unnecessary columns
df1 = df1.drop(['DATE'], axis=1)
df2 = df2.drop(['DATE'], axis=1)
df3 = df3.drop(['DATE', 'Compensation'], axis=1)  # Adjust column names as needed

# Merge datasets on 'Financial Quarter'
merged_df = pd.merge(df1, df2, on='Financial Quarter')
merged_df = pd.merge(merged_df, df3, on='Financial Quarter')

# Display the merged data
print(merged_df.head())
from PyEMD import EMD
import matplotlib.pyplot as plt

# EMD Analysis for GDP
gdp = merged_df['GDP'].values
emd = EMD()
imfs = emd(gdp)

# Plot the original signal and IMFs
plt.figure(figsize=(23, 13))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(merged_df['Financial Quarter'], gdp, 'r')
plt.title("Original Signal - GDP")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(merged_df['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()

# EMD Analysis for Compensation
CIB = merged_df['Compensation in Billions'].values
imfs = emd(CIB)

# Plot the original signal and IMFs
plt.figure(figsize=(12, 8))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(merged_df['Financial Quarter'], CIB, 'r')
plt.title("Original Signal - Compensation in Billions")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(merged_df['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()

# EMD Analysis for Employment Rate
ER = merged_df['Employement Rate'].values
imfs = emd(ER)

# Plot the original signal and IMFs
plt.figure(figsize=(12, 8))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(merged_df['Financial Quarter'], ER, 'r')
plt.title("Original Signal - Employment Rate")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(merged_df['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()
# Perform statistical analysis on IMFs (example: mean, standard deviation)
for i, imf in enumerate(imfs):
    print(f"IMF {i + 1}: Mean = {imf.mean()}, Std Dev = {imf.std()}")
# Example of generating a report of findings
import pandas as pd

report_data = {
    'IMF': [f'IMF {i + 1}' for i in range(len(imfs))],
    'Mean': [imf.mean() for imf in imfs],
    'Standard Deviation': [imf.std() for imf in imfs]
}
report_df = pd.DataFrame(report_data)

# Save report to CSV
report_df.to_csv('/content/IMF_Analysis_Report.csv', index=False)

print("IMF Analysis Report Generated")
