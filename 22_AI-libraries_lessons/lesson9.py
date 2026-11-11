
# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Step 2: Create dataset
X = np.array([
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [8, 9, 10],
    [9, 10, 11]
])

# Step 3: Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Create PCA model
pca = PCA(n_components=2)

# Step 5: Reduce dimensions
X_pca = pca.fit_transform(X_scaled)

# Step 6: Display reduced data
print("Reduced Data:")
print(X_pca)

# Step 7: Visualize the result
plt.figure(figsize=(8, 5))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    color='blue',
    s=100
)

# Step 8: Add graph details
plt.title("PCA - Dimensionality Reduction")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(alpha=0.3)

# Step 9: Display graph
plt.show()
