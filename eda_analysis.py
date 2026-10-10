
import pandas as pd
import os

# Load the sales dataset
file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)

# Display the first five rows
print("FIRST FIVE ROWS")
print(df.head())

# Check dataset size
print("\nDATASET SHAPE")
print(df.shape)

# Check column names and data types
print("\nDATASET INFORMATION")
df.info()

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Generate statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe(include="all"))

# Save initial analysis
os.makedirs("outputs", exist_ok=True)
df.describe(include="all").to_csv(
    "outputs/dataset_summary.csv"
)

print("\nAnalysis completed successfully!")
