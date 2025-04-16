import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'DHV Practical/Data/GlobalLandTemperaturesByCountry.csv'
df = pd.read_csv(file_path)

# Convert date column to datetime
df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year

# Drop rows where 'AverageTemperature' is missing
df_cleaned = df.dropna(subset=['AverageTemperature'])

# 1. Temperature Trends Over Time for Different Regions (Line Plot)
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_cleaned, x='Year', y='AverageTemperature', hue='Country', legend=False)
plt.title('Temperature Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.show()

# 2. Distribution of Missing Temperature Records Per Year (Bar Plot)
missing_per_year = df.groupby('Year')['AverageTemperature'].apply(lambda x: x.isna().sum())
plt.figure(figsize=(12, 6))
sns.barplot(x=missing_per_year.index, y=missing_per_year.values, hue=missing_per_year.index, palette='viridis', legend=False)
plt.xticks(rotation=90)
plt.title('Missing Temperature Records Per Year')
plt.xlabel('Year')
plt.ylabel('Count of Missing Records')
plt.show()

# 3. Anomalies in Precipitation Values (Box Plot)
if 'Precipitation' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Year', y='Precipitation', showfliers=True)
    plt.xticks(rotation=90)
    plt.title('Precipitation Anomalies Over Time')
    plt.xlabel('Year')
    plt.ylabel('Precipitation')
    plt.show()

# 4. Dual-axis plot for Temperature and Precipitation Patterns (Line Plot with Twin Axes)
if 'Precipitation' in df.columns and not df['Precipitation'].isna().all():
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()
    sns.lineplot(data=df_cleaned, x='Year', y='AverageTemperature', ax=ax1, color='r', label='Temperature')
    sns.lineplot(data=df_cleaned, x='Year', y='Precipitation', ax=ax2, color='b', label='Precipitation')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Temperature (°C)', color='r')
    ax2.set_ylabel('Precipitation', color='b')
    plt.title('Temperature and Precipitation Patterns')
    plt.show()

# 5. Heatmap of Correlations Between Climate Factors
climate_factors = df_cleaned[['AverageTemperature']].copy()
if 'AverageTemperatureUncertainty' in df.columns:
    climate_factors['AverageTemperatureUncertainty'] = df['AverageTemperatureUncertainty']
plt.figure(figsize=(8, 6))
sns.heatmap(climate_factors.corr(), annot=True, cmap='coolwarm', linewidths=1.0)
plt.title('Correlation Heatmap of Climate Factors')
plt.show()

# 6. Time-Series Plots for Seasonal Climate Variations (Line Plot with Shading)
seasonal_df = df_cleaned.copy()
seasonal_df['Month'] = seasonal_df['dt'].dt.month
plt.figure(figsize=(12, 6))
sns.lineplot(data=seasonal_df, x='Month', y='AverageTemperature', hue='Year', alpha=0.3)
plt.title('Seasonal Climate Variations')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()

# 7. Regional Trends in Extreme Weather Events (Histogram of Temperature Variability)
extreme_events = df_cleaned.groupby(['Country', 'Year'])['AverageTemperature'].std().reset_index()
plt.figure(figsize=(12, 6))
sns.histplot(data=extreme_events, x='AverageTemperature', bins=50, kde=True)
plt.title('Regional Trends in Extreme Weather Events')
plt.xlabel('Temperature Variability (°C)')
plt.ylabel('Frequency')
plt.show()

# 8. Visualization of Imputed Missing Temperature Data (Histogram)
df_imputed = df.copy()
df_imputed['AverageTemperature'] = df_imputed['AverageTemperature'].fillna(df_imputed.groupby('Country')['AverageTemperature'].transform('mean'))
plt.figure(figsize=(12, 6))
sns.histplot(df_imputed['AverageTemperature'], bins=50, kde=True, color='purple')
plt.title('Distribution of Imputed Temperature Data')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

# 9. Variance Before and After Cleaning Data (Box Plot)
plt.figure(figsize=(12, 6))
sns.boxplot(data=[df['AverageTemperature'].dropna(), df_imputed['AverageTemperature']], notch=True)
plt.xticks([0, 1], ['Original', 'Imputed'])
plt.title('Variance Before and After Cleaning Data')
plt.ylabel('Temperature (°C)')
plt.show()

# 10. Climate Data Trends for Top 5 Countries with Most Complete Records (Line Plot)
top_countries = df_cleaned['Country'].value_counts().head(5).index
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_cleaned[df_cleaned['Country'].isin(top_countries)], x='Year', y='AverageTemperature', hue='Country')
plt.title('Climate Data Trends for Top 5 Countries with Most Complete Records')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.show()
