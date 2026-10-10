
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Create output folder
os.makedirs("outputs", exist_ok=True)

sns.set_theme(style="whitegrid")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date column
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

# Ensure numeric sales columns
for col in ["quantity", "unit_price", "total_price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 1. Sales distribution
plt.figure(figsize=(9, 5))
sns.histplot(df["total_price"].dropna(), kde=True)
plt.title("Sales Distribution")
plt.xlabel("Total Price")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("outputs/01_sales_distribution.png", dpi=300)
plt.close()

# 2. Top 10 products by sales
product_sales = (
    df.groupby("product_name")["total_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/02_top_products.png", dpi=300)
plt.close()

# 3. Sales by region
region_sales = df.groupby("region")["total_price"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/03_sales_by_region.png", dpi=300)
plt.close()

# 4. Monthly sales trend
monthly_sales = (
    df.dropna(subset=["order_date"])
    .set_index("order_date")["total_price"]
    .resample("MS")
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/04_monthly_sales_trend.png", dpi=300)
plt.close()

# 5. Sales by category
category_sales = df.groupby("category")["total_price"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/05_sales_by_category.png", dpi=300)
plt.close()

# 6. Quantity vs total price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="quantity", y="total_price")
plt.title("Quantity vs Total Price")
plt.tight_layout()
plt.savefig("outputs/06_quantity_vs_sales.png", dpi=300)
plt.close()

# 7. Average unit price by category
avg_price = df.groupby("category")["unit_price"].mean()

plt.figure(figsize=(8, 5))
avg_price.plot(kind="bar")
plt.title("Average Unit Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Unit Price")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/07_avg_unit_price.png", dpi=300)
plt.close()

print("All visualizations completed!")
print("Files saved:")
for filename in sorted(os.listdir("outputs")):
    print(filename)
