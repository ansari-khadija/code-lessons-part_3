
# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Step 2: Create dataset
X = np.array([
    [1, 2], [2, 2], [2, 3],
    [3, 2], [3, 3],
    [8, 8], [8, 9], [9, 8],
    [9, 9], [10, 9],
    [20, 20]
])

# Step 3: Create DBSCAN model
model = DBSCAN(eps=2, min_samples=3)

# Step 4: Train the model
labels = model.fit_predict(X)

# Step 5: Visualize the clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels,
    cmap='viridis',
    s=100
)

# Step 6: Add graph details
plt.title("DBSCAN Clustering")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(alpha=0.3)

# Step 7: Display graph
plt.show()

# Step 8: Display cluster labels
print("Cluster Labels:", labels)
