import numpy as np

print("=== 1. Broadcasting ===")
a = np.array([1,2,3,4,5,6])
print(a+5)

print("=== 2. Broadcasting with two arrays ===")
a1 = np.array([1,11,2,22,3,33])
print("Substraction:",a - a1)
print("Addition:",a + a1)
print("Multiplication:",a * a1)

print("=== 3. Broadcasting 1D with 2D arrays ===")
import numpy as np

a2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
a3 = np.array([1, 2, 3])
print(a2 + a3)

print("=== 4. Broadcasting with columns ===")
a4 = np.array([
    [1],
    [2],
    [3]
])
print(a2 + a4)