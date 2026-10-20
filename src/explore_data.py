
# Import pandas for data analysis
import pandas as pd

# Load the dataset
df = pd.read_csv("data/product_quality_synthetic_dataset.csv")

# 1. Display the first five records
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# 2. Check the dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Check column names and data types
print("\n--- DATASET INFORMATION ---")
df.info()

# 4. Count missing values in each column
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 5. Count duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

# 6. Calculate statistics for numerical columns
print("\n--- SUMMARY STATISTICS ---")
print(df.describe().round(2))

# 7. Count unique values in each column
print("\n--- UNIQUE VALUES ---")
print(df.nunique())

# 8. Check whether sample IDs are unique
print("\n--- SAMPLE ID CHECK ---")
print("Unique sample IDs:", df["sample_id"].nunique())
