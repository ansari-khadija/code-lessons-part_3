import numpy as np

# Create two vectors
A = np.array([2, 4, 6])
B = np.array([1, 3, 5])

# Addition
print("Addition:", A + B)

# Subtraction
print("Subtraction:", A - B)

# Dot product
print("Dot Product:", np.dot(A, B))

# Magnitude
print("Magnitude:", np.linalg.norm(A))

# Cosine similarity
cosine = np.dot(A, B) / (
    np.linalg.norm(A) * np.linalg.norm(B)
)

print("Cosine Similarity:", cosine)