import pandas as pd

payments = pd.read_csv("data/olist_order_payments_dataset.csv")

print("=" * 60)
print("PAYMENTS DATASET ANALYSIS")
print("=" * 60)

print("\n--- SHAPE ---")
print("Rows:", payments.shape[0])
print("Columns:", payments.shape[1])

print("\n--- COLUMNS ---")
print(payments.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(payments.head())

print("\n--- DATA TYPES ---")
print(payments.dtypes)

print("\n--- MISSING VALUES ---")
print(payments.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", payments.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
for column in payments.columns:
    print(column, ":", payments[column].nunique())

print("\n--- PAYMENT METHODS ---")
print(payments["payment_type"].value_counts())

print("\n--- PAYMENT VALUE ---")
print(payments["payment_value"].describe())

print("\n--- INSTALLMENTS ---")
print(payments["payment_installments"].value_counts().sort_index())

print("\n--- INVALID VALUES ---")
print("Payment value <= 0:", (payments["payment_value"] <= 0).sum())
print("Installments <= 0:", (payments["payment_installments"] <= 0).sum())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)

print("\n--- ZERO/NEGATIVE PAYMENT VALUES ---")
print(
    payments[payments["payment_value"] <= 0]
)

print("\n--- ZERO/NEGATIVE INSTALLMENTS ---")
print(
    payments[payments["payment_installments"] <= 0]
)