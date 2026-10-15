# =====================================================
# DATA SCIENCE - PROGRAM 7
# TOPIC: DATA AGGREGATION
# =====================================================

# -----------------------------------------------------
# Import pandas library
# -----------------------------------------------------
# pandas is used for data manipulation and analysis.
# It provides the DataFrame structure which looks like
# a table containing rows and columns.
import pandas as pd

# -----------------------------------------------------
# Create a DataFrame
# -----------------------------------------------------
# A DataFrame is a two-dimensional table.
#
# Category Column:
# A
# A
# B
# B
#
# Data Column:
# 10
# 20
# 30
# 40
#
# Each value in Category corresponds to a value in Data.
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Data': [10, 20, 30, 40]
})

# -----------------------------------------------------
# Display Original Data
# -----------------------------------------------------
print("Original DataFrame:")
print(df)

# -----------------------------------------------------
# GroupBy Operation
# -----------------------------------------------------
# groupby() groups rows having the same Category value.
#
# Group A -> [10, 20]
# Group B -> [30, 40]
grouped = df.groupby('Category')

# -----------------------------------------------------
# Sum Aggregation
# -----------------------------------------------------
# Select the Data column from each group.
# sum() calculates the total value for every group.
#
# A = 10 + 20 = 30
# B = 30 + 40 = 70
print("\nSum of Data by Category:")
print(grouped['Data'].sum())

# -----------------------------------------------------
# Multiple Aggregations
# -----------------------------------------------------
# agg() allows multiple statistical operations.
#
# mean = average value
# std  = standard deviation
#
# Category A:
# mean = (10 + 20)/2 = 15
#
# Category B:
# mean = (30 + 40)/2 = 35
print("\nMean and Standard Deviation:")
print(grouped['Data'].agg(['mean', 'std']))