import pandas as pd

# Load the cybersecurity network dataset
# Ensure your CSV file is in the same folder or update the path below
df = pd.read_csv("Cleaned_Cyber_Security_Dataset1.csv")

# 1. Structural Audit
# Establishing the dataset architecture (1,779 network instances)
print("--- Dataset Information ---")
print(df.info())
print("\n--- Summary Statistics ---")
print(df.describe())

# 2. Data Cleaning & Integrity Checks
# Critical for security analysis to ensure no missing logs or duplicate entries
print("\n--- Integrity Check: Null Values ---")
print(df.isnull().sum())

print("\n--- Integrity Check: Duplicate Rows ---")
print(df.duplicated().sum())

# 3. Statistical Profiling for Anomaly Detection
# High Skewness and Kurtosis often indicate non-standard network behavior
print("\n--- Advanced Distribution Metrics ---")
print(f"App Bytes Skewness: {df['APP_BYTES'].skew():.2f}")
print(f"App Bytes Kurtosis: {df['APP_BYTES'].kurt():.2f}")

# 4. Feature Inspection
# Previewing the processed data
print("\n--- Cleaned Data Preview ---")
print(df.head())
