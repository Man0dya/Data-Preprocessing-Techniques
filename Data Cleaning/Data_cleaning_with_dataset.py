import pandas as pd

# Load dataset from CSV
df = pd.read_csv("sample_dirty_dataset.csv")
print("Original Data:\n", df)

# --- Handling Missing Values ---
# Fill missing Age with mean value
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Salary with median value
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# --- Handling Noisy Data ---
# Replace negative salary values with absolute value (or drop them if preferred)
df["Salary"] = df["Salary"].apply(lambda x: abs(x) if x < 0 else x)

print("\nCleaned Data:\n", df)
