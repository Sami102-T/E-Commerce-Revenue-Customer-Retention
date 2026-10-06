import pandas as pd

DATA_PATH = "data"

print("=" * 70)
print("E-COMMERCE COMPLETE DATA CLEANING")
print("=" * 70)


# ============================================================
# 1. LOAD DATA
# ============================================================

customers = pd.read_csv(f"{DATA_PATH}/olist_customers_dataset.csv")
orders = pd.read_csv(f"{DATA_PATH}/olist_orders_dataset.csv")
items = pd.read_csv(f"{DATA_PATH}/olist_order_items_dataset.csv")
products = pd.read_csv(f"{DATA_PATH}/olist_products_dataset.csv")
payments = pd.read_csv(f"{DATA_PATH}/olist_order_payments_dataset.csv")
reviews = pd.read_csv(f"{DATA_PATH}/olist_order_reviews_dataset.csv")
sellers = pd.read_csv(f"{DATA_PATH}/olist_sellers_dataset.csv")
geolocation = pd.read_csv(f"{DATA_PATH}/olist_geolocation_dataset.csv")
translation = pd.read_csv(
    f"{DATA_PATH}/product_category_name_translation.csv"
)

print("\nAll datasets loaded!")


# ============================================================
# 2. REMOVE EXACT DUPLICATES
# ============================================================

customers = customers.drop_duplicates()
orders = orders.drop_duplicates()
items = items.drop_duplicates()
products = products.drop_duplicates()
payments = payments.drop_duplicates()
reviews = reviews.drop_duplicates()
sellers = sellers.drop_duplicates()
geolocation = geolocation.drop_duplicates()
translation = translation.drop_duplicates()


# ============================================================
# 3. CLEAN ORDERS
# ============================================================

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 60 * 60)

orders["late_delivery"] = (
    orders["order_delivered_customer_date"]
    > orders["order_estimated_delivery_date"]
)


# ============================================================
# 4. CLEAN ORDER ITEMS
# ============================================================

items["shipping_limit_date"] = pd.to_datetime(
    items["shipping_limit_date"],
    errors="coerce"
)

items = items[
    (items["price"] >= 0) &
    (items["freight_value"] >= 0)
].copy()

items["total_item_value"] = (
    items["price"] + items["freight_value"]
)


# ============================================================
# 5. CLEAN PRODUCTS
# ============================================================

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("unknown")
)

numeric_product_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in numeric_product_columns:
    products[col] = products[col].fillna(
        products[col].median()
    )

products.loc[
    products["product_weight_g"] <= 0,
    "product_weight_g"
] = products["product_weight_g"].median()


# ============================================================
# 6. CLEAN CUSTOMERS
# ============================================================

customers["customer_city"] = (
    customers["customer_city"]
    .str.strip()
    .str.lower()
)

customers["customer_state"] = (
    customers["customer_state"]
    .str.strip()
    .str.upper()
)


# ============================================================
# 7. CLEAN SELLERS
# ============================================================

sellers["seller_city"] = (
    sellers["seller_city"]
    .str.strip()
    .str.lower()
)

sellers["seller_state"] = (
    sellers["seller_state"]
    .str.strip()
    .str.upper()
)


# ============================================================
# 8. CLEAN PAYMENTS
# ============================================================

payments = payments[
    payments["payment_value"] >= 0
].copy()

# Create payment summary per order
payment_summary = payments.groupby("order_id").agg(
    total_payment_value=("payment_value", "sum"),
    payment_count=("payment_sequential", "count"),
    max_installments=("payment_installments", "max")
).reset_index()

# Most common payment method per order
payment_method = (
    payments.groupby("order_id")["payment_type"]
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else "unknown")
    .reset_index()
)

payment_summary = payment_summary.merge(
    payment_method,
    on="order_id",
    how="left"
)

print("\nPayment summary created.")


# ============================================================
# 9. CLEAN REVIEWS
# ============================================================

reviews["review_comment_title"] = (
    reviews["review_comment_title"]
    .fillna("")
)

reviews["review_comment_message"] = (
    reviews["review_comment_message"]
    .fillna("")
)

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

# Review summary per order
review_summary = reviews.groupby("order_id").agg(
    average_review_score=("review_score", "mean"),
    review_count=("review_score", "count")
).reset_index()

print("Review summary created.")


# ============================================================
# 10. CLEAN GEOLOCATION
# ============================================================

geolocation["geolocation_city"] = (
    geolocation["geolocation_city"]
    .str.strip()
    .str.lower()
)

geolocation["geolocation_state"] = (
    geolocation["geolocation_state"]
    .str.strip()
    .str.upper()
)

# One location record per ZIP prefix
geo_summary = geolocation.groupby(
    "geolocation_zip_code_prefix"
).agg(
    latitude=("geolocation_lat", "mean"),
    longitude=("geolocation_lng", "mean"),
    geo_city=("geolocation_city", "first"),
    geo_state=("geolocation_state", "first")
).reset_index()

print("Geolocation summary created.")


# ============================================================
# 11. CLEAN CATEGORY TRANSLATION
# ============================================================

translation["product_category_name"] = (
    translation["product_category_name"]
    .str.strip()
    .str.lower()
)

translation["product_category_name_english"] = (
    translation["product_category_name_english"]
    .str.strip()
    .str.lower()
)


# ============================================================
# 12. CREATE MAIN SALES DATASET
# ============================================================

master = orders.merge(
    items,
    on="order_id",
    how="left"
)

master = master.merge(
    products,
    on="product_id",
    how="left"
)

master = master.merge(
    translation,
    on="product_category_name",
    how="left"
)

master = master.merge(
    customers,
    on="customer_id",
    how="left"
)

master = master.merge(
    sellers,
    on="seller_id",
    how="left"
)


# ============================================================
# 13. ADD PAYMENT INFORMATION
# ============================================================

master = master.merge(
    payment_summary,
    on="order_id",
    how="left"
)


# ============================================================
# 14. ADD REVIEW INFORMATION
# ============================================================

master = master.merge(
    review_summary,
    on="order_id",
    how="left"
)


# ============================================================
# 15. ADD CUSTOMER GEOLOCATION
# ============================================================

master = master.merge(
    geo_summary,
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix",
    how="left"
)


# ============================================================
# 16. ADD SELLER GEOLOCATION
# ============================================================

seller_geo = geo_summary.rename(
    columns={
        "geolocation_zip_code_prefix":
            "seller_geo_zip_code_prefix",
        "latitude":
            "seller_latitude",
        "longitude":
            "seller_longitude",
        "geo_city":
            "seller_geo_city",
        "geo_state":
            "seller_geo_state"
    }
)

master = master.merge(
    seller_geo,
    left_on="seller_zip_code_prefix",
    right_on="seller_geo_zip_code_prefix",
    how="left"
)


# ============================================================
# 17. BUSINESS COLUMNS
# ============================================================

master["revenue"] = master["price"]

master["revenue_with_freight"] = (
    master["price"] +
    master["freight_value"]
)

master["purchase_date"] = (
    master["order_purchase_timestamp"].dt.date
)

master["purchase_year"] = (
    master["order_purchase_timestamp"].dt.year
)

master["purchase_month"] = (
    master["order_purchase_timestamp"].dt.month
)

master["year_month"] = (
    master["order_purchase_timestamp"]
    .dt.to_period("M")
    .astype(str)
)


# ============================================================
# 18. FINAL CHECK
# ============================================================

print("\n" + "=" * 70)
print("FINAL MASTER DATASET")
print("=" * 70)

print("\nShape:")
print(master.shape)

print("\nRows:", len(master))
print("Columns:", len(master.columns))

print("\nDuplicate rows:")
print(master.duplicated().sum())

print("\nTop missing values:")
print(
    master.isnull()
    .sum()
    .sort_values(ascending=False)
    .head(20)
)

print("\nProduct Revenue:")
print(round(master["revenue"].sum(), 2))


# ============================================================
# 19. SAVE FINAL MASTER FILE
# ============================================================

master.to_csv(
    f"{DATA_PATH}/master_complete.csv",
    index=False
)

print("\n" + "=" * 70)
print("COMPLETE MASTER DATASET CREATED!")
print("=" * 70)

print("\nFile:")
print("data/master_complete.csv")