# DATA SCIENCE - Program 4
# Data Wrangling

# Import pandas for data manipulation
import pandas as pd

# Import numpy for numerical operations and random number generation
import numpy as np

# ----------------------------
# A. Hierarchical Indexing
# ----------------------------

# Create a Series with random values and a hierarchical (multi-level) index
data = pd.Series(
    np.random.randn(6),
    index=[['a', 'a', 'b', 'b', 'c', 'c'],
           [1, 2, 1, 2, 1, 2]]
)

# Display the complete Series
print('Original Series:')
print(data)

# Display all values belonging to index 'b'
print('\nValues for index b:')
print(data['b'])

# Display values where second-level index equals 1
print('\nValues with second index = 1:')
print(data[:, 1])

# ----------------------------
# B. Stack and Unstack
# ----------------------------

# Convert hierarchical Series into DataFrame
df = data.unstack()

# Display unstacked DataFrame
print('\nUnstacked DataFrame:')
print(df)

# Convert DataFrame back to Series
print('\nStacked Series:')
print(df.stack())

# ----------------------------
# C. Merge and Combine
# ----------------------------

# Create first DataFrame with missing values
df1 = pd.DataFrame({'a': [1, np.nan, 3], 'b': [4, 5, 6]})

# Create second DataFrame with missing values
df2 = pd.DataFrame({'a': [7, 8, 9], 'b': [np.nan, 11, 12]})

# Combine DataFrames and fill missing values in df1 using df2
merged = df1.combine_first(df2)

# Display merged DataFrame
print('\nMerged DataFrame:')
print(merged)