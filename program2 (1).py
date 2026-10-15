# Import the requests library to send HTTP requests
import requests
# Import pandas for DataFrame operations
import pandas as pd

# GitHub API URL for pandas issues
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

# Send GET request to GitHub API
response = requests.get(url)
# Convert JSON response to Python object
issues = response.json()

# Create DataFrame from issues data
df_issues = pd.DataFrame(issues)

# Display selected columns from first 5 records
print(df_issues[['id', 'title', 'state', 'created_at']].head())

# Import SQLite library
import sqlite3

# Connect to database (creates file if it does not exist)
conn = sqlite3.connect('students.db')

# Create cursor object
cursor = conn.cursor()

# Create students table if it does not already exist
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)")

# Insert first record
cursor.execute("INSERT INTO students VALUES (2, 'MBU')")

# Save changes
conn.commit()

# Insert second record
cursor.execute("INSERT INTO students VALUES (2, 'Joy')")

# Save changes
conn.commit()

# Read table data into DataFrame
df = pd.read_sql_query('SELECT * FROM students', conn)

# Display table data
print(df)

import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")

# Create a cursor object
cursor = conn.cursor()

# Update student name where id = 1
cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    ("Alice", 1)
)

# Delete student with id = 1
cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (1,)
)

# Save (commit) the changes
conn.commit()

# Close the cursor
cursor.close()

# Close the database connection
conn.close()

import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table (if it does not exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Insert second record
cursor.execute("INSERT INTO students (id, name) VALUES (?, ?)", (2, 'Joy'))

# Save changes
conn.commit()

# Read table data into DataFrame
df = pd.read_sql_query("SELECT * FROM students", conn)

# Display table data
print("Before Update:")
print(df)

# Update student name where id = 1
cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    ("Alice", 1)
)

# Save the update
conn.commit()

# Read updated table data
df = pd.read_sql_query("SELECT * FROM students", conn)

# Display updated table data
print("\nAfter Update:")
print(df)

# Close the connection
conn.close()