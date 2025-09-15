import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

# ==================================
# 1. DATA CLEANING
# ==================================
print("\n--- DATA CLEANING ---")

# Dataset with missing + noisy values
dirty_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, np.nan, 35, 40, np.nan, 29],
    "Salary": [35000, -10000, 48000, np.nan, 60000, 72000]
}
df_dirty = pd.DataFrame(dirty_data)
print("Original Dirty Data:\n", df_dirty)

# Fill missing Age with mean
df_dirty["Age"].fillna(df_dirty["Age"].mean(), inplace=True)

# Fill missing Salary with median
df_dirty["Salary"].fillna(df_dirty["Salary"].median(), inplace=True)

# Fix noisy data (negative salary → absolute value)
df_dirty["Salary"] = df_dirty["Salary"].apply(lambda x: abs(x))
print("\nCleaned Data:\n", df_dirty)

# ==================================
# 2. DATA TRANSFORMATION (Normalization)
# ==================================
print("\n--- DATA TRANSFORMATION ---")

transform_data = {
    "Age": [25, 32, 47, 51, 62, 29, 41, 55, 60, 38],
    "Salary": [35000, 48000, 56000, 60000, 72000, 40000, 52000, 65000, 70000, 45000]
}
df_transform = pd.DataFrame(transform_data)
print("Original Data:\n", df_transform)

# Min-Max Normalization
scaler = MinMaxScaler()
df_transform["Salary_MinMax"] = scaler.fit_transform(df_transform[["Salary"]])

# Z-Score Normalization
zscaler = StandardScaler()
df_transform["Salary_Zscore"] = zscaler.fit_transform(df_transform[["Salary"]])

print("\nNormalized Data:\n", df_transform)

# ==================================
# 3. DATA REDUCTION (PCA + Sampling)
# ==================================
print("\n--- DATA REDUCTION ---")

np.random.seed(42)
reduction_data = {
    "ID": range(1, 101),
    "Feature1": np.random.randint(10, 100, 100),
    "Feature2": np.random.randint(200, 500, 100),
    "Feature3": np.random.uniform(1.5, 9.5, 100),
    "Feature4": np.random.randint(1000, 5000, 100),
    "Feature5": np.random.uniform(50, 150, 100),
}
df_reduction = pd.DataFrame(reduction_data)
print("Original Reduction Dataset (first 5 rows):\n", df_reduction.head())

# Standardize before PCA
scaled = StandardScaler().fit_transform(df_reduction.drop("ID", axis=1))

# Apply PCA (reduce to 2 components)
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled)
df_reduced = pd.DataFrame(reduced_data, columns=["PC1", "PC2"])
print("\nAfter PCA (first 5 rows):\n", df_reduced.head())

# Sampling (take 30% random sample)
sampled = df_reduction.sample(frac=0.3, random_state=42)
print("\nSampled Data (30% of dataset):\n", sampled.head())

# ==================================
# 4. DATA INTEGRATION
# ==================================
print("\n--- DATA INTEGRATION ---")

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Country": ["USA", "UK", "Canada", "USA"]
})

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 1, 3, 4],
    "Amount": [250, 450, 300, 150, 500]
})

print("Customers:\n", customers)
print("\nOrders:\n", orders)

# Merge (Integration)
integrated = pd.merge(customers, orders, on="CustomerID", how="inner")
print("\nIntegrated Dataset:\n", integrated)

# ==================================
# 5. OTHER DATA PREPROCESSING TECHNIQUES
# ==================================
print("\n--- OTHER DATA PREPROCESSING TECHNIQUES ---")

# Example: Binning (Discretization)
other_data = {
    "Age": [25, 32, 47, 51, 62, 29, 41, 55, 60, 38]
}
df_other = pd.DataFrame(other_data)
# Create age bins
bins = [20, 30, 40, 50, 60, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60-69']
df_other['AgeGroup'] = pd.cut(df_other['Age'], bins=bins, labels=labels, right=False)
print("Binning (Discretization) Example:\n", df_other)

# Example: Encoding categorical variables
cat_data = {
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
}
df_cat = pd.DataFrame(cat_data)
df_cat_encoded = pd.get_dummies(df_cat, columns=["Color"])
print("\nOne-Hot Encoding Example:\n", df_cat_encoded)
