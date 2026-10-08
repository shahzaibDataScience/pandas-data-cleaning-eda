"""
Pandas Data Cleaning & EDA — Foundation Project
================================================
Goal: take a MESSY sales CSV, clean it step by step, then explore it.

Run:  python data_cleaning_eda.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# STEP 1: Load the data and take a first look
# =========================================================
# Always inspect first: df.head() shows sample rows,
# df.info() reveals missing values AND wrong data types.
df = pd.read_csv("data/sales_data.csv")

print("=== First 5 rows ===")
print(df.head())
print("\n=== Shape (rows, columns):", df.shape)
print("\n=== Info (check missing values + dtypes) ===")
print(df.info())

# =========================================================
# STEP 2: Handle missing values
# =========================================================
print("\n=== Missing values per column ===")
print(df.isnull().sum())

# Quantity: only 2 missing out of ~20 rows -> fill with median
# (median is safer than mean: one huge order won't skew it)
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# City: 1 missing -> we can't guess a city, so drop that row
df = df.dropna(subset=["City"])

# Salesperson: 3 missing -> label them "Unknown" instead of dropping
# (dropping would lose real sales records)
df["Salesperson"] = df["Salesperson"].fillna("Unknown")

# =========================================================
# STEP 3: Remove duplicate rows
# =========================================================
# NOTE: OrderID 1002 appears twice -> same order counted twice
# would inflate our sales numbers. drop_duplicates() fixes it.
before = len(df)
df = df.drop_duplicates()
print(f"\nRemoved {before - len(df)} duplicate row(s)")

# =========================================================
# STEP 4: Fix inconsistent text (City column)
# =========================================================
# "Lahore", "lahore", "LAHORE " are the SAME city, but for
# groupby() they are 3 different groups! Standardize:
# strip() removes extra spaces, title() -> "Lahore" format.
print("\n=== City values BEFORE cleaning ===")
print(df["City"].unique())

df["City"] = df["City"].str.strip().str.title()

print("\n=== City values AFTER cleaning ===")
print(df["City"].unique())

# =========================================================
# STEP 5: Fix wrong data types (Price column)
# =========================================================
# Some prices are "Rs.35000" (text). Remove "Rs." and convert
# to numbers, otherwise math on this column will fail.
df["Price"] = (
    df["Price"].astype(str)          # make everything text first
    .str.replace("Rs.", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)                  # now convert to numbers
)

# Date column -> proper datetime so we can analyze by month
df["Date"] = pd.to_datetime(df["Date"])

# =========================================================
# STEP 6: Create a Revenue column & explore (EDA)
# =========================================================
df["Revenue"] = df["Quantity"] * df["Price"]

print("\n=== Cleaned data info ===")
print(df.info())
print("\n=== Summary stats ===")
print(df.describe())

print("\n=== Total revenue by city ===")
print(df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

print("\n=== Total revenue by product ===")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print("\n=== Monthly revenue trend ===")
monthly = df.set_index("Date").resample("ME")["Revenue"].sum()
print(monthly)

# =========================================================
# STEP 7: Visualize
# =========================================================
sns.set_theme(style="whitegrid")

# Chart 1: Revenue by city (bar chart)
plt.figure(figsize=(8, 4))
df.groupby("City")["Revenue"].sum().sort_values().plot(kind="barh", color="teal")
plt.title("Total Revenue by City")
plt.xlabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("revenue_by_city.png")
print("\nSaved chart: revenue_by_city.png")

# Chart 2: Distribution of order quantities (histogram)
plt.figure(figsize=(8, 4))
sns.histplot(df["Quantity"], bins=8, kde=True, color="coral")
plt.title("Distribution of Order Quantities")
plt.xlabel("Quantity")
plt.tight_layout()
plt.savefig("quantity_distribution.png")
print("Saved chart: quantity_distribution.png")

# =========================================================
# STEP 8: Save the cleaned dataset
# =========================================================
df.to_csv("data/sales_data_cleaned.csv", index=False)
print("\nSaved cleaned data: data/sales_data_cleaned.csv")
print("\nDone! Compare sales_data.csv vs sales_data_cleaned.csv")
