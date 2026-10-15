# DATA SCIENCE - Program 6
# Time Series Analysis

# Import pandas library for time series operations
import pandas as pd

# Import numpy library for generating random numbers
import numpy as np

# --------------------------------------------------
# A. Create Time Series
# --------------------------------------------------

# Create a date range starting from 2023-01-01
# periods=6 creates 6 dates
# freq='D' means daily frequency
rng = pd.date_range('2023-01-01', periods=6, freq='D')

# Generate random values and create a time series
ts = pd.Series(np.random.randn(len(rng)), index=rng)

# Display the time series
print("Time Series:")
print(ts)

# --------------------------------------------------
# B. Time Zone Conversion
# --------------------------------------------------

# Assign UTC timezone to the time series
ts_utc = ts.tz_localize('UTC')

# Convert UTC timezone to Indian Standard Time
ts_ind = ts_utc.tz_convert('Asia/Kolkata')

# Display converted time series
print("\nTime Series in Asia/Kolkata:")
print(ts_ind)

# --------------------------------------------------
# C. Period Arithmetic and Conversion
# --------------------------------------------------

# Create a quarterly period representing Q1 of 2024
p = pd.Period('2024Q1')

# Add one quarter to the period
print("\nNext Quarter:")
print(p + 1)

# Convert the quarterly period to month-end frequency
print("\nQuarter End Month:")
print(p.asfreq('M', 'end'))

# --------------------------------------------------
# D. Resampling
# --------------------------------------------------

# Create a time series with 100 daily random values
ts = pd.Series(
    np.random.randn(100),
    index=pd.date_range('2024-01-01', periods=100)
)

# Resample daily data into monthly averages
ts_monthly = ts.resample('ME').mean()

# Display monthly averages
print("\nMonthly Average Values:")
print(ts_monthly)