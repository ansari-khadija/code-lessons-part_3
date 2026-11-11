
# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 2: Create dataset
X = np.array([
    [1, 2],
    [2, 3],
    [3, 2],
    [8, 8],
    [9, 10],
    [10, 9]
])

# Step 3: Apply Hierarchical Clustering
linked = linkage(X, method='ward')

# Step 4: Draw Dendrogram
plt.figure(figsize=(8, 5))

dendrogram(
    linked,
    labels=['A', 'B', 'C', 'D', 'E', 'F'],
    color_threshold=5
)

# Step 5: Add graph details
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.grid(axis='y', alpha=0.3)

# Step 6: Display graph
plt.show()
