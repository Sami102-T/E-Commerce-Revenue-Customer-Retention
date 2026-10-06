import pandas as pd

# Load customer dataset
customers = pd.read_csv("data/olist_customers_dataset.csv")

# Basic information
print("Shape:", customers.shape)

print("\nColumns:")
print(customers.columns)

print("\nFirst 5 rows:")
print(customers.head())

print("\nData types:")
print(customers.dtypes)

print("\nMissing values:")
print(customers.isnull().sum())

print("\nDuplicate rows:")
print(customers.duplicated().sum())

print("Duplicate rows:", customers.duplicated().sum())
print("Unique customer_id:", customers["customer_id"].nunique())
print("Unique customer_unique_id:", customers["customer_unique_id"].nunique())