
import pandas as pd
import os

# Load sales dataset
df = pd.read_csv("data/sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert columns to correct data types
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

for col in ["quantity", "unit_price", "total_price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate orders
df = df.drop_duplicates()

# Remove rows without essential sales information
df = df.dropna(
    subset=["order_date", "quantity", "unit_price", "total_price"]
)

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Export cleaned data
df.to_csv("outputs/cleaned_sales_data.csv", index=False)
df.to_excel("outputs/cleaned_sales_data.xlsx", index=False)

print("Dashboard data prepared successfully!")
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print("Saved cleaned_sales_data.csv")
print("Saved cleaned_sales_data.xlsx")
