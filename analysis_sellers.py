import pandas as pd

# Load sellers dataset
sellers = pd.read_csv("data/olist_sellers_dataset.csv")

print("=" * 60)
print("SELLERS DATASET ANALYSIS")
print("=" * 60)

print("\n--- SHAPE ---")
print("Rows:", sellers.shape[0])
print("Columns:", sellers.shape[1])

print("\n--- COLUMNS ---")
print(sellers.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(sellers.head())

print("\n--- DATA TYPES ---")
print(sellers.dtypes)

print("\n--- MISSING VALUES ---")
print(sellers.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", sellers.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
for column in sellers.columns:
    print(column, ":", sellers[column].nunique())

print("\n--- NUMERICAL SUMMARY ---")
print(sellers.describe())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)