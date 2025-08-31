# Customers dataset

customers = {
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Country": ["USA", "UK", "Canada", "USA"]
}
df_customers = pd.DataFrame(customers)
file_path_customers = "/mnt/data/customers.csv"
df_customers.to_csv(file_path_customers, index=False)

# Orders dataset
orders = {
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 1, 3, 4],
    "Amount": [250, 450, 300, 150, 500]
}
df_orders = pd.DataFrame(orders)
file_path_orders = "/mnt/data/orders.csv"
df_orders.to_csv(file_path_orders, index=False)

file_path_customers, file_path_orders
