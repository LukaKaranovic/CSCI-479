import sys

# Redirect stdout to file.
sys.stdout = open('eda_results.txt', 'w')

# # Assignment 1 - Exploratory Data Analysis of German Credit Dataset
# 
# First, we import the required Python libraries and load the dataset. We will be working with the `GermanCredit_Dataset.xlsx` file.


import pandas as pd
import numpy as np

# We load the specific 'Data' sheet from the Excel file 
    # Metadata/title rows at the top are skipped using skiprows
    # Only the columns we care about (that contain information) are loaded using usecols
df = pd.read_excel(
    'GermanCredit_Dataset.xlsx',
    sheet_name='Data',      
    skiprows=1,             
    usecols='B:V',
    header=0 # Tell pandas that the first selected row contains column names          
)

print("View first 5 rows of the DataFrame to ensure it loaded correctly.")
print('=' * 80)

print(df.head())

 
print("\n=== Metadata Analysis ===\n")
# 
# We will now check for basic information about our table:
# - For each column: 
#     - the name
#     - the data type stored in the column
#     - the data item count (number of non-null values)


# Check basic info (row count, non-null counts, and data types)
df.info()

print('=' * 80)

 
print("\n=== Missing Attribute Analysis ===\n")
# 
# For each attribute, we will find:
# - Count of missing values
# - The percentage of missing values


# Check the exact count of missing values per column
print("# of Missing Values per Column:")
missing_counts = df.isnull().sum()
for col, count in missing_counts.items():
    # left-aligns the column name in a 15-character space
    print(f"{col:<25} | {count}")

print("-" * 40) # Divider line for clarity

# Calculate the percentage of missing values (if any)
print("Missing Percentage per Column:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
for col, pct in missing_percentage.items():

    # {pct:.2f} rounds the percentage to 2 decimal places
    print(f"{col:<25} | {pct:.2f}%")

 
print("\n=== Analyzing Categorical Attributes ===\n")
# 
# For each categorical attribute, our goal in this section is to find:
# 
# 1. The total number of unique values appearing under this attribute.
# 2. The exact list of unique values and how many times each one appears in the dataset (their frequency).


# Loop through all columns that are stored as objects (strings/categories)
for col in df.select_dtypes(include=['object', 'category']).columns:
    print(f"=== Attribute: {col} ===")
    
    # 1. Find the number of unique values
    cardinality = df[col].nunique()
    print(f"Number of categories: {cardinality}")
    
    # 2. Get each unique value and its frequency count
    print(f"{'Value':<35} | Frequency")
    print("-" * 50) 
    counts = df[col].value_counts()
    
    # Loop through each unique value and its count
    for val, freq in counts.items():
        print(f"{val:<35} | {freq}")
    print("=" * 80) 

 
print("\n=== Analyzing Numeric Attributes ===\n")
# 
# For any numeric attribute with **less than or equal to 5 unique values**, we will find:
# 
# 1. The total number of unique values appearing under this attribute.
# 2. The exact list of unique values and how many times each one appears in the dataset (their frequency).
# 
# For any numeric attribute with **more than 5 unique values**, we will find:
# 
# 1. **Range, Min, and Max**: The smallest value, largest value, and the span between them.
# 2. **Average**: The arithmetic mean.
# 3. **Three Most Frequent Values**: The three most common values in that column and how many times they appear.


# Loop through all columns that contain numbers
for col in df.select_dtypes(include=[np.number]).columns:
    print(f"=== Attribute: {col} ===")

    # If numerical field has more than 
    if df[col].nunique() > 5:
    # 1. Find Min, Max, and Range
        min_val = df[col].min()
        max_val = df[col].max()
        range_val = max_val - min_val
        print(f"Range: {range_val} (Min: {min_val}, Max: {max_val})")
        
        # 2. Find Average (Mean)
        avg_val = df[col].mean()
        print(f"Average: {avg_val:.2f}")
        
        # 3. Find top three most frequent values and their frequencies
        top_three = df[col].value_counts().head(3) # Fetch top 3 rows
        print(f"Top {len(top_three)} most frequent values:")
        for val, freq in top_three.items():
            print(f"{val:<10} | {freq}")
    else:
        # 1. Find the number of unique values
        cardinality = df[col].nunique()
        print(f"Number of categories: {cardinality}")
        
        # 2. Get each unique value and its frequency count
        print(f"{'Value':<35} | Frequency")
        print("-" * 50) 
        counts = df[col].value_counts()
        
        # Loop through each unique value and its count
        for val, freq in counts.items():
            print(f"{val:<35} | {freq}")

    print("=" * 80)

 
print("\n=== Discretization of continuous 'age' attribute ===\n")
# 
# Based on the reasons I described in my report, I will split the bins into 10 year intervals. To make it easier to interpret, I will start near the 'decade' marker (E.g. 19-28 instead of 16-25). Since the minimum age in the dataset is 19, and the maximum is 75, we will have these bins:
# 
# - **19–28:** Young adults / starting careers
# - **29–38:** Establishing careers / family building
# - **39–48:** Peak career / mid-life stability
# - **49–58:** Late career / pre-retirement
# - **59–68:** Traditional retirement age
# - **69–78:** Post-retirement / fixed income
# 


# Define strictly equal-width bins (Every bin has a width of exactly 10 years)
bins = [19, 28, 38, 48, 58, 68, 78]
labels = ['19-28', '29-38', '39-48', '49-58', '59-68', '69-78']

# Use pd.cut to create discretized column
    # include_lowest is so lowest value (19) gets included
df['age_bracket'] = pd.cut(df['age'], bins=bins, labels=labels, right=True, include_lowest=True)

# Get frequencyes for each age bracket
age_counts = df['age_bracket'].value_counts().sort_index()

# Output frequency table
print(f"{'Age Bracket':<15} | Frequency")
print("-" * 50) 
for bracket, freq in age_counts.items():
    print(f"{str(bracket):<15} | {freq}")

print("=" * 80)
