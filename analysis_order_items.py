import pandas as pd

# Load order items dataset
items = pd.read_csv("data/olist_order_items_dataset.csv")

print("=" * 60)
print("ORDER ITEMS DATASET ANALYSIS")
print("=" * 60)

# 1. Shape
print("\n--- SHAPE ---")
print("Rows:", items.shape[0])
print("Columns:", items.shape[1])

# 2. Columns
print("\n--- COLUMNS ---")
print(items.columns.tolist())

# 3. First 5 rows
print("\n--- FIRST 5 ROWS ---")
print(items.head())

# 4. Data types
print("\n--- DATA TYPES ---")
print(items.dtypes)

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(items.isnull().sum())

# 6. Duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", items.duplicated().sum())

# 7. Unique values
print("\n--- UNIQUE VALUES ---")
for column in items.columns:
    print(column, ":", items[column].nunique())

# 8. Basic statistics
print("\n--- NUMERICAL SUMMARY ---")
print(items.describe())

# 9. Check negative/zero prices
print("\n--- PRICE CHECK ---")
print("Price <= 0:", (items["price"] <= 0).sum())

# 10. Check negative/zero freight
print("\n--- FREIGHT CHECK ---")
print("Freight value < 0:", (items["freight_value"] < 0).sum())

# 11. Price statistics
print("\n--- PRICE STATISTICS ---")
print("Minimum price:", items["price"].min())
print("Maximum price:", items["price"].max())
print("Average price:", items["price"].mean())

# 12. Freight statistics
print("\n--- FREIGHT STATISTICS ---")
print("Minimum freight:", items["freight_value"].min())
print("Maximum freight:", items["freight_value"].max())
print("Average freight:", items["freight_value"].mean())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)