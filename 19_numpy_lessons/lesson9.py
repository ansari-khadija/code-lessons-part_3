import numpy as np

print("=== A. split ===")
a = np.array([10, 20, 30, 40, 50, 60])
result = np.split(a, 3)
print(result)

print("=== B. array splitting ===")
for item in result:
    print(item)

print("=== C. hsplit() ===")
a1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result2 = np.hsplit(a1, 2)
for item in result2:
    print(item)

print("=== D. vsplit() ===")

result3 = np.vsplit(a1, 2)
for item in result3:
    print(item)