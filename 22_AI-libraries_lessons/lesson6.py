
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Customer data
X = np.array([
    [15, 20], [20, 25], [25, 30],
    [70, 80], [75, 85], [80, 90],
    [66, 89], [33, 40], [91, 22]
])

# Create K-Means model
model = KMeans(n_clusters=2, random_state=0, n_init=10)

# Train model
labels = model.fit_predict(X)

# Get cluster centres
centres = model.cluster_centers_

# Plot customer groups
plt.scatter(X[:, 0], X[:, 1],
            c=labels, cmap='viridis',
            s=100, label='Customers')

# Plot cluster centres as black circles
plt.scatter(centres[:, 0], centres[:, 1],
            color='black', marker='o',
            s=250, edgecolors='white',
            label='Cluster Centres')

# Add graph information
plt.title("Customer Segmentation Using K-Means")
plt.xlabel("Annual Income (in thousands)")
plt.ylabel("Spending Score")
plt.legend()
plt.grid(alpha=0.3)

plt.show()
