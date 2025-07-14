# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set visualization style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load the dataset
file_path = r"C:\Users\niran\OneDrive\Desktop\data analysis\research.csv"  # Use your actual file path
df = pd.read_csv(file_path)

# --------------------------
# Data Cleaning & Preprocessing
# --------------------------

# Convert RD_Value and Relative_Sampling_Error to numeric (handle non-numeric values)
df['RD_Value'] = pd.to_numeric(df['RD_Value'], errors='coerce')
df['Relative_Sampling_Error'] = pd.to_numeric(df['Relative_Sampling_Error'], errors='coerce')

# Drop rows with missing essential values
df_clean = df.dropna(subset=['RD_Value', 'Year', 'Breakdown_category'])

# --------------------------
# Basic Information
# --------------------------

print("📌 Dataset Info:\n")
print(df.info())
print("\n📌 Missing values per column:\n")
print(df.isnull().sum())
print("\n📌 Summary statistics:\n")
print(df.describe(include='all'))

# --------------------------
# Aggregated Insights
# --------------------------

# R&D Expenditure Over Time
rd_by_year = df_clean.groupby('Year')['RD_Value'].sum().reset_index()

# Top 10 Breakdown Categories by Total R&D Expenditure
top_sectors = df_clean.groupby('Breakdown_category')['RD_Value'].sum().nlargest(10).reset_index()

# --------------------------
# Visualization Section
# --------------------------

# 1. Total R&D Expenditure Over Years
plt.figure(figsize=(10, 5))
sns.lineplot(data=rd_by_year, x='Year', y='RD_Value', marker='o', color='teal')
plt.title('Total R&D Expenditure Over the Years')
plt.ylabel('RD Value (NZ$ Millions)')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

# 2. Top 10 Sectors by Total R&D Expenditure
plt.figure(figsize=(12, 6))
sns.barplot(data=top_sectors, x='RD_Value', y='Breakdown_category', palette='viridis')
plt.title('Top 10 Sectors by Total R&D Expenditure')
plt.xlabel('Total RD Value (NZ$ Millions)')
plt.ylabel('Sector')
plt.tight_layout()
plt.show()

# 3. Boxplot: Distribution of RD Value by Year
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean, x='Year', y='RD_Value', palette='Set3')
plt.title('Distribution of R&D Value by Year')
plt.ylabel('RD Value (NZ$ Millions)')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

# 4. Histogram: Relative Sampling Error Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Relative_Sampling_Error'], bins=30, kde=True, color='coral')
plt.title('Distribution of Relative Sampling Error')
plt.xlabel('Relative Sampling Error (%)')
plt.tight_layout()
plt.show()

# 5. Heatmap of Missing Values
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='YlGnBu')
plt.title("Heatmap of Missing Data")
plt.tight_layout()
plt.show()

# --------------------------
# Optional: Save Cleaned Data
# --------------------------

# df_clean.to_csv("cleaned_RD_data.csv", index=False)
