import pandas as pd

# Load customer and order data
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

print("Customers:\n", customers)
print("\nOrders:\n", orders)

# --- Data Integration: Merge on CustomerID ---
merged_df = pd.merge(customers, orders, on="CustomerID", how="inner")
print("\nIntegrated Data:\n", merged_df)
