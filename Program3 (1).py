# Data Science - Program 3
# Data Cleaning and Preparation

# -------------------------------
# A. Handle Missing Data
# -------------------------------

# Import NumPy for numerical operations and NaN values
import numpy as np

# Import pandas for DataFrame operations
import pandas as pd

# Create a dictionary containing missing values (np.nan)
data = {'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan]}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display True/False values indicating missing data locations
print(df.isna())

# Remove rows that contain missing values
df_clean = df.dropna()

# Replace missing values with 0
df_filled = df.fillna(0)

# Display DataFrame after removing missing values
print(df_clean)

# Display DataFrame after filling missing values
print(df_filled)

# -------------------------------
# B. Data Transformation
# -------------------------------

# Create a DataFrame with gender values
df = pd.DataFrame({'gender': ['male', 'female', 'male']})

# Convert categorical values into numerical values
df['gender_num'] = df['gender'].map({'male': 0, 'female': 1})

# Rename column gender to Gender
df_renamed = df.rename(columns={'gender': 'Gender'})

# Display transformed DataFrame
print(df_renamed)

# -------------------------------
# C. Outlier Detection
# -------------------------------

# Create 100x3 random numerical dataset
data = pd.DataFrame(np.random.randn(100, 3))

# Identify values greater than 3 or less than -3
outliers = (data > 3) | (data < -3)

# Display the number of outliers in each column
print(outliers.sum())

# -------------------------------
# D. Regex for Text Manipulation
# -------------------------------

# Import the regular expression module
import re

# Create a text string containing spaces, tab and newline characters
text = "This  itest"

# Split text using one or more whitespace characters
split_text = re.split(r'\s+', text)

# Display the split result
print(split_text)