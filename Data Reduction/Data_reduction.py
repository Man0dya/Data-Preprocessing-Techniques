import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("sample_reduction_dataset.csv")
print("Original Data:\n", df.head())

# --- Step 1: Standardize the data ---
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop("ID", axis=1))  # drop ID column

# --- Step 2: Apply PCA (reduce to 2 dimensions) ---
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

df_reduced = pd.DataFrame(reduced_data, columns=["PC1", "PC2"])
print("\nAfter PCA Reduction:\n", df_reduced.head())

# --- Step 3: Sampling (take 50% random sample) ---
sampled_df = df.sample(frac=0.5, random_state=42)
print("\nSampled Data (50%):\n", sampled_df)
