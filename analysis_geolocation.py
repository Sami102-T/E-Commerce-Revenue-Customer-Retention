import pandas as pd

geo = pd.read_csv("data/olist_geolocation_dataset.csv")

print("=" * 60)
print("GEOLOCATION DATASET ANALYSIS")
print("=" * 60)

print("\n--- SHAPE ---")
print("Rows:", geo.shape[0])
print("Columns:", geo.shape[1])

print("\n--- COLUMNS ---")
print(geo.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(geo.head())

print("\n--- DATA TYPES ---")
print(geo.dtypes)

print("\n--- MISSING VALUES ---")
print(geo.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", geo.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
for column in geo.columns:
    print(column, ":", geo[column].nunique())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)