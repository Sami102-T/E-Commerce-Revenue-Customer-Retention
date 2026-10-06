import pandas as pd

reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")

print("=" * 60)
print("REVIEWS DATASET ANALYSIS")
print("=" * 60)

print("\n--- SHAPE ---")
print("Rows:", reviews.shape[0])
print("Columns:", reviews.shape[1])

print("\n--- COLUMNS ---")
print(reviews.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(reviews.head())

print("\n--- DATA TYPES ---")
print(reviews.dtypes)

print("\n--- MISSING VALUES ---")
print(reviews.isnull().sum())

print("\n--- MISSING VALUE PERCENTAGE ---")
print((reviews.isnull().sum() / len(reviews) * 100).round(2))

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", reviews.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
for column in reviews.columns:
    print(column, ":", reviews[column].nunique())

print("\n--- REVIEW SCORE ---")
print(reviews["review_score"].value_counts().sort_index())

print("\n--- REVIEW SCORE SUMMARY ---")
print(reviews["review_score"].describe())

print("\n--- INVALID REVIEW SCORES ---")
print(
    reviews[
        (reviews["review_score"] < 1) |
        (reviews["review_score"] > 5)
    ]
)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)