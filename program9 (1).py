# ==============================================================
# DATA SCIENCE - PROGRAM 9
# CASE STUDY: CUSTOMER PERSONALITY ANALYSIS USING K-MEANS
# ==============================================================

# AIM:
# ----
# To analyze customer purchasing behavior and divide customers
# into different groups (clusters) using the K-Means clustering
# algorithm.
#
# K-Means is an Unsupervised Machine Learning algorithm.
# It groups similar customers together without predefined labels.
#
# ==============================================================


# ==============================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ==============================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ==============================================================
# STEP 2: LOAD THE DATASET
# ==============================================================

# IMPORTANT:
# Use the RAW GitHub URL, not the GitHub /blob/ webpage URL.

url = "https://raw.githubusercontent.com/tirthajyoti/Machine-Learning-with-Python/master/Datasets/Mall_Customers.csv"

# Read CSV file
df = pd.read_csv(url)


# ==============================================================
# STEP 3: DISPLAY DATASET
# ==============================================================

print("=" * 70)
print("FIRST FIVE RECORDS")
print("=" * 70)

print(df.head())


print("\n")
print("=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

df.info()


print("\n")
print("=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


print("\n")
print("=" * 70)
print("COLUMN NAMES")
print("=" * 70)

print(df.columns.tolist())


# ==============================================================
# STEP 4: CHECK MISSING VALUES
# ==============================================================

print("\n")
print("=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(df.isnull().sum())


# ==============================================================
# STEP 5: CHECK DUPLICATE RECORDS
# ==============================================================

print("\n")
print("=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

print("Number of duplicate rows:", df.duplicated().sum())


# ==============================================================
# STEP 6: SELECT FEATURES FOR CLUSTERING
# ==============================================================

# We use:
#
# Annual Income (k$)
# Spending Score (1-100)
#
# These two variables are commonly used for customer segmentation.

X = df[
    [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]


print("\n")
print("=" * 70)
print("SELECTED FEATURES")
print("=" * 70)

print(X.head())


# ==============================================================
# STEP 7: STANDARDIZE THE FEATURES
# ==============================================================

# StandardScaler converts features into a common scale.
#
# This is useful because K-Means uses distance calculations.

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


print("\n")
print("=" * 70)
print("STANDARDIZED FEATURES")
print("=" * 70)

print(X_scaled[:5])


# ==============================================================
# STEP 8: ELBOW METHOD
# ==============================================================

# The Elbow Method helps determine a suitable number of clusters.

inertia = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertia.append(model.inertia__)


# Plot Elbow Curve

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    inertia,
    marker="o"
)

plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.grid(True)

plt.tight_layout()

plt.savefig("elbow_method.png")

plt.show()


# ==============================================================
# STEP 9: CREATE K-MEANS MODEL
# ==============================================================

# Based on the elbow method, we select 5 clusters.

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)


# ==============================================================
# STEP 10: TRAIN MODEL AND ASSIGN CLUSTERS
# ==============================================================

# fit_predict():
#
# fit()         -> trains the K-Means model
# predict()     -> assigns cluster numbers
#
# fit_predict() performs both operations.

df["Cluster"] = kmeans.fit_predict(X_scaled)


# ==============================================================
# STEP 11: DISPLAY CUSTOMER CLUSTERS
# ==============================================================

print("\n")
print("=" * 70)
print("CUSTOMER CLUSTERS")
print("=" * 70)

print(
    df[
        [
            "CustomerID",
            "Annual Income (k$)",
            "Spending Score (1-100)",
            "Cluster"
        ]
    ].head(20)
)


# ==============================================================
# STEP 12: DISPLAY CLUSTER CENTERS
# ==============================================================

# Cluster centers are initially calculated
# in standardized feature space.
#
# Convert them back to the original scale
# for easier interpretation.

cluster_centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)

centers_df = pd.DataFrame(
    cluster_centers,
    columns=[
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
)

centers_df.index.name = "Cluster"


print("\n")
print("=" * 70)
print("CLUSTER CENTERS")
print("=" * 70)

print(centers_df)



# ==============================================================
# STEP 13: COUNT CUSTOMERS IN EACH CLUSTER
# ==============================================================

print("\n")
print("=" * 70)
print("CUSTOMER COUNT PER CLUSTER")
print("=" * 70)

print(df["Cluster"].value_counts().sort_index())


# ==============================================================
# STEP 14: CUSTOMER SEGMENT SUMMARY
# ==============================================================

summary = df.groupby("Cluster")[
    [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
].mean()

summary["Customer Count"] = df["Cluster"].value_counts()

summary = summary.sort_index()


print("\n")
print("=" * 70)
print("CUSTOMER SEGMENT SUMMARY")
print("=" * 70)

print(summary)


# ==============================================================
# STEP 15: VISUALIZE CUSTOMER SEGMENTS
# ==============================================================

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="tab10",
    s=100
)


# Plot cluster centers

plt.scatter(
    cluster_centers[:, 0],
    cluster_centers[:, 1],
    marker="X",
    s=250,
    c="black",
    label="Cluster Centers"
)


plt.title(
    "Customer Personality Analysis using K-Means",
    fontsize=15
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "customer_segments_kmeans.png",
    dpi=300
)

plt.show()


# ==============================================================
# STEP 16: SAVE CLUSTERED DATASET
# ==============================================================

df.to_csv(
    "Mall_Customers_Clustered.csv",
    index=False
)


# ==============================================================
# STEP 17: FINAL MESSAGE
# ==============================================================

print("\n")
print("=" * 70)
print("CUSTOMER SEGMENTATION COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Number of Clusters :", kmeans.n_clusters)

print("Clustered dataset saved as:")
print("Mall_Customers_Clustered.csv")

print("\nGraphs saved as:")
print("1. elbow_method.png")
print("2. customer_segments_kmeans.png")