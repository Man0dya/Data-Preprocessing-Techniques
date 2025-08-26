import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset from CSV
df = pd.read_csv("sample_dataset.csv")
print("Original Data:\n", df)

# --- 1. Min-Max Normalization (scale values between 0 and 1) ---
min_max_scaler = MinMaxScaler()
df["Salary_MinMax"] = min_max_scaler.fit_transform(df[["Salary"]])

# --- 2. Z-Score Normalization (mean=0, std=1) ---
zscore_scaler = StandardScaler()
df["Salary_Zscore"] = zscore_scaler.fit_transform(df[["Salary"]])

print("\nAfter Normalization:\n", df)
