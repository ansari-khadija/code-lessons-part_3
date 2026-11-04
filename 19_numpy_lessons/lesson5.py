
import numpy as np

# ==========================================
# LESSON 4: INDEXING AND SLICING
# ==========================================

print("\n===== 1D ARRAY INDEXING =====")

a = np.array([10, 20, 30, 40, 50])

# Positive indexing
print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[4])

# Negative indexing
print("Last element:", a[-1])
print("Second last:", a[-2])

# ==========================================
# 1D ARRAY SLICING
# ==========================================

print("\n===== 1D ARRAY SLICING =====")

print("First three:", a[0:3])
print("From index 2:", a[2:])
print("Before index 3:", a[:3])
print("Every second element:", a[::2])
print("Reverse array:", a[::-1])

# ==========================================
# 2D ARRAY INDEXING
# ==========================================

print("\n===== 2D ARRAY INDEXING =====")

b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Complete array:\n", b)

# Access individual elements
print("First row, first column:", b[0, 0])
print("Second row, second column:", b[1, 1])
print("Third row, third column:", b[2, 2])

# Access complete rows
print("First row:", b[0])
print("Second row:", b[1])

# Access complete columns
print("First column:", b[:, 0])
print("Second column:", b[:, 1])

# ==========================================
# 2D ARRAY SLICING
# ==========================================

print("\n===== 2D ARRAY SLICING =====")

print("First two rows:\n", b[:2, :])

print("First two columns:\n", b[:, :2])

print("First two rows and columns:\n", b[:2, :2])

print("Last two rows:\n", b[1:, :])

# ==========================================
# 3D ARRAY INDEXING
# ==========================================

print("\n===== 3D ARRAY INDEXING =====")

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Complete 3D array:\n", c)

# Access individual elements
print("First element:", c[0, 0, 0])
print("Last element:", c[1, 1, 1])

# Access 2D matrices
print("First matrix:\n", c[0])
print("Second matrix:\n", c[1])

# Access a specific row
print("First row of second matrix:", c[1, 0])

# Access specific column
print("First column of first matrix:", c[0, :, 0])

# ==========================================
# LESSON 5: BOOLEAN INDEXING AND FILTERING
# ==========================================

print("\n===== BOOLEAN INDEXING =====")

marks = np.array([35, 80, 45, 90, 25, 70, 95])

# Boolean condition
print("Marks greater than 50:", marks > 50)

# Filter values
print("Passed students:", marks[marks >= 40])

print("Failed students:", marks[marks < 40])

print("Excellent students:", marks[marks >= 90])

# ==========================================
# MULTIPLE CONDITIONS
# ==========================================

print("\n===== MULTIPLE CONDITIONS =====")

# Marks between 40 and 80
result = marks[(marks >= 40) & (marks <= 80)]

print("Marks between 40 and 80:", result)

# Marks below 40 OR above 90
result2 = marks[(marks < 40) | (marks > 90)]

print("Below 40 or above 90:", result2)

# NOT condition
result3 = marks[~(marks < 40)]

print("Marks NOT below 40:", result3)

# ==========================================
# NP.WHERE()
# ==========================================

print("\n===== NP.WHERE() =====")

prices = np.array([100, 250, 500, 750, 1000])

# Find indexes where price > 300
indexes = np.where(prices > 300)

print("Indexes:", indexes)

# Find matching values
print("Matching prices:", prices[indexes])

# Replace values conditionally
discounted = np.where(prices >= 500, prices * 0.9, prices)

print("Discounted prices:", discounted)

# ==========================================
# NP.ANY() AND NP.ALL()
# ==========================================

print("\n===== ANY AND ALL =====")

print("Any price above 900:", np.any(prices > 900))

print("All prices positive:", np.all(prices > 0))