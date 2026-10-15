import pandas as pd
from io import StringIO

# Read CSV file from URL
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)
print(df.head())

# Write CSV to file
df.to_csv("output.csv", index=False)

# Reading and Writing JSON Data
json_data = df.to_json()
df_json = pd.read_json(StringIO(json_data))
print(df_json.head())

# Reading and Writing Excel Files
df.to_excel("output.xlsx", index=False)
df_excel = pd.read_excel("output.xlsx")
print(df_excel.head())