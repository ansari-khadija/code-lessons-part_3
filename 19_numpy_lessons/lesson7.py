import numpy as np
 
print("=== 1. Axis concepts – axis=0 and axis=1 ===")
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(a)
print("Example 1: Sum")
print("Total:", np.sum(a))
print("Column totals:", np.sum(a, axis=0))
print("Row totals:", np.sum(a, axis=1))

print("Example 2: Mean, maximum and minimum")
print("Column average:", np.mean(a, axis=0))
print("Row average:", np.mean(a, axis=1))
print("Column maximum:", np.max(a, axis=0))
print("Row minimum:", np.min(a, axis=1))

print("Example 3: Other useful operations")
print("Column standard deviation:", np.std(a, axis=0))
print("Row standard deviation:", np.std(a, axis=1))