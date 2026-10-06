import pandas as pd

translation = pd.read_csv(
    "data/product_category_name_translation.csv"
)

print("=" * 60)
print("CATEGORY TRANSLATION ANALYSIS")
print("=" * 60)

print("\n--- SHAPE ---")
print("Rows:", translation.shape[0])
print("Columns:", translation.shape[1])

print("\n--- COLUMNS ---")
print(translation.columns.tolist())

print("\n--- FIRST 10 ROWS ---")
print(translation.head(10))

print("\n--- DATA TYPES ---")
print(translation.dtypes)

print("\n--- MISSING VALUES ---")
print(translation.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", translation.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
for column in translation.columns:
    print(column, ":", translation[column].nunique())