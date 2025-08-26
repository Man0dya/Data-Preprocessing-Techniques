import numpy as np

# Generate dataset with 100 rows, 5 numerical features
np.random.seed(42)
data = {
    "ID": range(1, 101),
    "Feature1": np.random.randint(10, 100, 100),
    "Feature2": np.random.randint(200, 500, 100),
    "Feature3": np.random.uniform(1.5, 9.5, 100),
    "Feature4": np.random.randint(1000, 5000, 100),
    "Feature5": np.random.uniform(50, 150, 100),
}

df = pd.DataFrame(data)
file_path_reduction = "/mnt/data/sample_reduction_dataset.csv"
df.to_csv(file_path_reduction, index=False)
file_path_reduction
