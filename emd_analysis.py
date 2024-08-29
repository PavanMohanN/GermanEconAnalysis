import pandas as pd
import matplotlib.pyplot as plt
from PyEMD import EMD

# Load and preprocess datasets
df1 = pd.read_csv('/content/Employement Germany Modified.csv')  # Replace with your actual file path
df2 = pd.read_csv('/content/GDP Germany Modified.csv')          # Replace with your actual file path
df3 = pd.read_csv('/content/Compensation Germany Modified.csv')

df1 = df1.drop('DATE', axis=1)
df2 = df2.drop('DATE', axis=1)
df3 = df3.drop('DATE', axis=1)
df3 = df3.drop('Compensation', axis=1)

# Merge datasets
merged_df = pd.merge(df1, df2, on='Financial Quarter')
merged_df = pd.merge(merged_df, df3, on='Financial Quarter')

# Plot GDP, Compensation, and Employment Rate
fig, ax1 = plt.subplots(figsize=(23, 13))
ax1.plot(merged_df['Financial Quarter'], merged_df['Employement Rate'], color='red')
ax1.set_xlabel('Financial Quarter')
ax1.set_ylabel('Employement Rate', color="red")
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.plot(merged_df['Financial Quarter'], merged_df['GDP'], color='blue')
ax2.set_ylabel('GDP', color="blue")
ax2.tick_params(axis='y', labelcolor='blue')

ax3 = ax1.twinx()
ax3.plot(merged_df['Financial Quarter'], merged_df['Compensation in Billions'], color='green')
ax3.spines['right'].set_position(('axes', 1.06))
ax3.set_ylabel('Compensation in Billions', color="green")
ax3.tick_params(axis='y', labelcolor='green')

fig.autofmt_xdate()
fig.tight_layout()
fig.savefig('combined_plot.png')
plt.show()

# Plot GDP vs Compensation
fig, ax1 = plt.subplots(figsize=(23, 13))
ax1.plot(merged_df['Financial Quarter'], merged_df['Employement Rate'], color='red')
ax1.set_xlabel('Financial Quarter')
ax1.set_ylabel('Employement Rate', color="red")
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.plot(merged_df['Financial Quarter'], merged_df['GDP'], color='blue')
ax2.set_ylabel('GDP', color="blue")
ax2.tick_params(axis='y', labelcolor='blue')

fig.autofmt_xdate()
plt.show()

# Plot Compensation vs Employment Rate
fig, ax1 = plt.subplots(figsize=(23, 13))
ax1.plot(merged_df['Financial Quarter'], merged_df['Employement Rate'], color='red')
ax1.set_xlabel('Financial Quarter')
ax1.set_ylabel('Employement Rate', color="red")
ax1.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.plot(merged_df['Financial Quarter'], merged_df['Compensation in Billions'], color='green')
ax3.set_ylabel('Compensation in Billions', color="green")
ax3.tick_params(axis='y', labelcolor='green')

fig.autofmt_xdate()
fig.tight_layout()
fig.savefig('compensation_employment_plot.png')
plt.show()

# EMD Analysis for GDP
data = pd.read_csv('/content/GDP Germany Modified.csv')
gdp = data['GDP'].values
emd = EMD()
imfs = emd(gdp)

plt.figure(figsize=(23, 13))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(data['Financial Quarter'], gdp, 'r')
plt.title("Original Signal - GDP")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(data['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()

# EMD Analysis for Compensation
data = pd.read_csv('/content/Compensation Germany Modified.csv')
data['DATE'] = pd.to_datetime(data['DATE'])
CIB = data['Compensation in Billions'].values
emd = EMD()
imfs = emd(CIB)

plt.figure(figsize=(12, 8))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(data['Financial Quarter'], CIB, 'r')
plt.title("Original Signal - Compensation in Billions")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(data['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()

# EMD Analysis for Employment Rate
data = pd.read_csv('/content/Employement Germany Modified.csv')
data['DATE'] = pd.to_datetime(data['DATE'])
ER = data['Employement Rate'].values
emd = EMD()
imfs = emd(ER)

plt.figure(figsize=(12, 8))
plt.subplot(len(imfs) + 1, 1, 1)
plt.plot(data['Financial Quarter'], ER, 'r')
plt.title("Original Signal - Employment Rate")

for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 2)
    plt.plot(data['Financial Quarter'], imf, 'g')
    plt.title(f"IMF {i + 1}")

plt.tight_layout()
plt.show()
