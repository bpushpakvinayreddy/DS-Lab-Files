# DATA SCIENCE - Program 5
# Data Visualization with Matplotlib and Seaborn

# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# ---------------------------
# A. Line Plot
# ---------------------------

# X-axis values
x = [1, 2, 3, 4]

# Y-axis values
y = [10, 20, 25, 30]

# Create a line plot using x and y values
plt.plot(x, y)

# Add a title to the graph
plt.title('Line Plot')

# Set label for X-axis
plt.xlabel('X-axis')

# Set label for Y-axis
plt.ylabel('Y-axis')

# Display grid lines
plt.grid(True)

# Save the plot as an image file
plt.savefig('/mnt/data/line_plot.png')
plt.close()

# ---------------------------
# B. Bar Plot
# ---------------------------

# Import pandas for DataFrame creation
import pandas as pd

# Create sample categorical data
df = pd.DataFrame({'Category':['A','B','C'],'Values':[10,20,15]})

# Create a bar chart
df.plot(kind='bar', x='Category', y='Values')

# Add chart title
plt.title('Bar Plot')

# Save the plot
plt.savefig('/mnt/data/bar_plot.png')
plt.close()

# ---------------------------
# C. Histogram and Density Plot
# ---------------------------

# Import seaborn for statistical visualization
import seaborn as sns

# Import numpy for random data generation
import numpy as np

# Generate 1000 random values
data = np.random.randn(1000)

# Create histogram with KDE curve
sns.histplot(data, kde=True)

# Add title
plt.title('Histogram and Density')

# Save figure
plt.savefig('/mnt/data/histogram_density.png')
plt.close()

# ---------------------------
# D. Scatter Plot
# ---------------------------

# Generate random x values
x = np.random.rand(50)

# Generate random y values
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# Save figure
plt.savefig('/mnt/data/scatter_plot.png')
plt.close()

# ---------------------------
# E. Box Plot
# ---------------------------

# Create box plot from random data
sns.boxplot(data=np.random.randn(100,4))

# Add chart title
plt.title('Box Plot')

# Save figure
plt.savefig('/mnt/data/box_plot.png')
plt.close()

print('All visualizations generated successfully.')