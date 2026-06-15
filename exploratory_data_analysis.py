import pandas as pd
import numpy as np

# 1. Load the dataset (Cleaned or Raw, here we use the original file provided)
file_path = 'Dataset for Data Analytics.xlsx - Sheet1.csv'
df = pd.read_csv(file_path)

print("=== PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA) ===")

# 2. Descriptive Statistics (Mean, Median, Count)
# This uncovers the "center of gravity" of our numerical data as required by DecodeLabs
print("\n[1] Descriptive Statistics for TotalPrice and Quantity:")
numerical_summary = df[['Quantity', 'UnitPrice', 'TotalPrice']].describe().loc[['count', 'mean', '50%']]
numerical_summary.rename(index={'50%': 'median'}, inplace=True)
print(numerical_summary.round(2))

# 3. Identify Outliers (The anomalies/extreme values)
# Using the IQR (Interquartile Range) method to find extreme order totals
q1 = df['TotalPrice'].quantile(0.25)
q3 = df['TotalPrice'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)
lower_bound = q1 - (1.5 * iqr)

outliers = df[(df['TotalPrice'] > upper_bound) | (df['TotalPrice'] < lower_bound)]
print(f"\n[2] Outlier Detection (TotalPrice):")
print(f"   - Upper threshold for normal orders: ${upper_bound:.2f}")
print(f"   - Number of extreme outlier orders identified: {len(outliers)}")

# 4. Trend Analysis: Top Performing Products & Payment Methods
print("\n[3] Revenue and Order Count by Product Category:")
product_trends = df.groupby('Product').agg(
    Total_Revenue=('TotalPrice', 'sum'),
    Order_Count=('OrderID', 'count')
).sort_values(by='Total_Revenue', ascending=False)
print(product_trends.round(2))

print("\n[4] Order Status Breakdown:")
status_breakdown = df['OrderStatus'].value_counts()
print(status_breakdown)

# 5. Exporting Summary Metrics to a Text File for Documentation
with open('EDA_Summary_Report.txt', 'w') as report:
    report.write("=== DECODELABS INTERNSHIP: PROJECT 2 SUMMARY REPORT ===\n")
    report.write(f"Total Records Analyzed: {len(df)}\n\n")
    report.write("[DESCRIPTIVE STATISTICS]\n")
    report.write(numerical_summary.to_string() + "\n\n")
    report.write("[PRODUCT PERFORMANCE TRENDS]\n")
    report.write(product_trends.to_string() + "\n\n")
    report.write(f"[OUTLIER INSIGHTS]\nTotal Outlier Orders Found: {len(outliers)}\n")

print("\nEDA Report successfully generated and saved as 'EDA_Summary_Report.txt'.")
