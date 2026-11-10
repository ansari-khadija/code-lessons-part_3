import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix Addition
print("Addition:")
print(A + B)

# Matrix Subtraction
print("Subtraction:")
print(A - B)

# Matrix Multiplication
print("Multiplication:")
print(np.matmul(A, B))

# Transpose
print("Transpose:")
print(A.T)

# Determinant
print("Determinant:")
print(np.linalg.det(A))

# Inverse
print("Inverse:")
print(np.linalg.inv(A))

# Eigenvalues
print("Eigenvalues:")
print(np.linalg.eigvals(A))