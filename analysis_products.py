import pandas as pd

# Load products dataset
products = pd.read_csv("data/olist_products_dataset.csv")

print("=" * 60)
print("PRODUCTS DATASET ANALYSIS")
print("=" * 60)

# 1. Shape
print("\n--- SHAPE ---")
print("Rows:", products.shape[0])
print("Columns:", products.shape[1])

# 2. Columns
print("\n--- COLUMNS ---")
print(products.columns.tolist())

# 3. First 5 rows
print("\n--- FIRST 5 ROWS ---")
print(products.head())

# 4. Data types
print("\n--- DATA TYPES ---")
print(products.dtypes)

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(products.isnull().sum())

# 6. Missing percentage
print("\n--- MISSING VALUE PERCENTAGE ---")
print((products.isnull().sum() / len(products) * 100).round(2))

# 7. Duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", products.duplicated().sum())

# 8. Unique values
print("\n--- UNIQUE VALUES ---")
for column in products.columns:
    print(column, ":", products[column].nunique())

# 9. Numerical summary
print("\n--- NUMERICAL SUMMARY ---")
print(products.describe())

# 10. Check invalid dimensions
dimension_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

print("\n--- INVALID / ZERO VALUES ---")

for column in dimension_columns:
    print(
        column,
        "zero values:",
        (products[column] == 0).sum()
    )

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)