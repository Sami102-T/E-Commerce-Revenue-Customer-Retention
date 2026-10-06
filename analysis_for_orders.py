import pandas as pd

orders = pd.read_csv("data/olist_orders_dataset.csv")

print("Shape:", orders.shape)
print("\nColumns:")
print(orders.columns)

print("\nMissing values:")
print(orders.isnull().sum())

print("\nDuplicate rows:")
print(orders.duplicated().sum())

print("\nData types:")
print(orders.dtypes)

print("\n--- ORDER STATUS ---")
print(orders["order_status"].value_counts())

print("\n--- MISSING DELIVERY DATE BY STATUS ---")
print(
    orders.groupby("order_status")[
        "order_delivered_customer_date"
    ].apply(lambda x: x.isna().sum())
)
print(
    orders[
        (orders["order_status"] == "delivered") &
        (orders["order_delivered_customer_date"].isna())
    ]
)
# Convert date columns to datetime
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"],
    errors="coerce"
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"],
    errors="coerce"
)

# Keep only orders where actual delivery date is available
delivered_orders = orders[
    orders["order_delivered_customer_date"].notna()
].copy()

# Check whether each order was late
delivered_orders["late_delivery"] = (
    delivered_orders["order_delivered_customer_date"]
    > delivered_orders["order_estimated_delivery_date"]
)

# Count late and on-time orders
print("\n--- DELIVERY PERFORMANCE ---")
print(delivered_orders["late_delivery"].value_counts())

# Calculate late delivery rate
late_rate = delivered_orders["late_delivery"].mean() * 100

print("\nLate Delivery Rate:", round(late_rate, 2), "%")