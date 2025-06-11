#Interpreter: Pytho 3..11.9 64-bit (Microsoft Store)
#Libraries: pandas, matplotlib, seaborn, geopandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

#change as per your file dirctory
path_rain = r"C:\Users\tanya\Desktop\Tanya\Internship ss24\ss25\rainfall_mh_apr_jun24.csv" # rainfall dataset
path_tractor = r"C:\Users\tanya\Desktop\Tanya\Internship ss24\ss25\data_day_mh_apr_jun24.csv" # tractor dataset

# Load datasets
rain_df = pd.read_csv(path_rain)  
tractor_df = pd.read_csv(path_tractor)  

# Date formatting
rain_df['date'] = pd.to_datetime(rain_df['date'])
tractor_df['day'] = pd.to_datetime(tractor_df['day'])

# Helper to save plots
def save_plot(filename):
   # plt.show()
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

# Task 1: Daily Tractor Usage Trends
daily = tractor_df.groupby('day').agg({
    'total_engine_hrs': 'sum',
    'total_area_acres': 'sum'
}).reset_index()

rain_daily = rain_df.groupby('date')['precip_mm'].sum().reset_index()
combined = pd.merge(daily, rain_daily, left_on='day', right_on='date', how='left')

fig, ax1 = plt.subplots(figsize=(16, 7))
ax2 = ax1.twinx()

ax1.plot(combined['day'], combined['total_engine_hrs'], 'o-', color='tab:blue')
ax1.set_ylabel('Total Engine Hours', color='tab:blue')
ax2.plot(combined['day'], combined['precip_mm'], 's-', color='tab:purple')
ax2.set_ylabel('Total Rainfall (mm)', color='tab:purple')

plt.title("Task 1: Engine Hours and Rainfall per Day (Apr–Jun 2024)")
plt.xticks(rotation=45)
save_plot("task1_engine_hours_vs_rainfall.png") # can change name of file as needed


# Task 2: Regional Usage Patterns (Top 10 Districts)
district_totals = tractor_df.groupby('district')['total_area_acres'].sum().nlargest(10).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=district_totals, x='district', y='total_area_acres', palette='viridis')
plt.title('Task 2: Top 10 Districts by Total Acres Tilled')
plt.ylabel('Total Acres')
plt.xticks(rotation=45)
save_plot("task2_top10_districts_acres.png")


# Task 3: Rainfall vs Tractor Activity
merged = pd.merge(tractor_df, rain_df, left_on=['day', 'district'], right_on=['date', 'dt_name'])

# Scatter: Rain vs Acres
plt.figure(figsize=(8, 6))
sns.scatterplot(data=merged, x='precip_mm', y='total_area_acres')
plt.title('Task 3: Rainfall vs Acres Tilled')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Acres Tilled')
save_plot("task3_scatter_rain_vs_acres.png")

# Lag plot: rain[t-1] vs acres[t]
merged.sort_values('day', inplace=True)
merged['rain_t-1'] = merged.groupby('district')['precip_mm'].shift(1)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=merged, x='rain_t-1', y='total_area_acres')
plt.title('Task 3: Rainfall [t-1] vs Acres Tilled [t]')
plt.xlabel('Rainfall Previous Day (mm)')
plt.ylabel('Acres Tilled')
save_plot("task3_lagplot_rain_t-1_vs_acres.png")


# Task 4: Regional Rain Sensitivity
correlation = merged.groupby('district').apply(
    lambda df: df['precip_mm'].corr(df['total_area_acres'])
).dropna().reset_index(name='rain_acres_corr')

plt.figure(figsize=(12, 6))
sns.barplot(data=correlation.sort_values('rain_acres_corr', ascending=False), 
            x='rain_acres_corr', y='district', palette='coolwarm')
plt.title('Task 4: Rainfall-Acres Correlation by District')
plt.xlabel('Correlation Coefficient')
save_plot("task4_rain_acres_correlation.png")

# Task 5: Untimely Rain Event Impact
merged['untimely_rain'] = merged['precip_mm'] > 20

# Timeline: rainfall spikes + drop in acres
daily_summary = merged.groupby('day').agg({
    'precip_mm': 'sum',
    'total_area_acres': 'sum'
}).reset_index()

fig, ax1 = plt.subplots(figsize=(16, 7))
ax2 = ax1.twinx()
ax1.plot(daily_summary['day'], daily_summary['total_area_acres'], 'o-', color='tab:blue')
ax2.plot(daily_summary['day'], daily_summary['precip_mm'], 's-', color='tab:purple')
ax1.set_ylabel('Acres Tilled', color='tab:blue')
ax2.set_ylabel('Rainfall (mm)', color='tab:purple')
plt.title("Task 5: Rainfall Spikes vs Farming Activity")
plt.xticks(rotation=45)
save_plot("task5_rain_spikes_vs_activity.png")

# Boxplot: Untimely vs normal days
plt.figure(figsize=(8, 6))
sns.boxplot(data=merged, x='untimely_rain', y='total_area_acres')
plt.xticks([0, 1], ['Normal Days', 'Untimely Rain Days'])
plt.title('Task 5: Farming Activity on Untimely vs Normal Rain Days')
plt.ylabel('Acres Tilled')
save_plot("task5_boxplot_untimely_vs_normal.png")
