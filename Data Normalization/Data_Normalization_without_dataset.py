import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Sample dataset
data = {
    "Age": [25, 32, 47, 51, 62],
    "Salary": [35000, 48000, 56000, 60000, 72000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# --- 1. Min-Max Normalization (scale values between 0 and 1) ---
min_max_scaler = MinMaxScaler()
df["Salary_MinMax"] = min_max_scaler.fit_transform(df[["Salary"]])

# --- 2. Z-Score Normalization (standardization: mean=0, std=1) ---
zscore_scaler = StandardScaler()
df["Salary_Zscore"] = zscore_scaler.fit_transform(df[["Salary"]])

print("\nAfter Normalization:\n", df)
    