# NumPy and Mathematical Operations

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print("===== ARITHMETIC =====")
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))
print(np.sqrt(a))
print(np.square(a))

print("\n===== STATISTICS =====")
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.min(a))
print(np.max(a))

print("\n===== ARRAY =====")
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 10))
print(np.sort(a))
print(np.unique(a))

print("\n===== SEARCHING =====")
print(np.where(a > 25))
print(np.argmax(a))
print(np.argmin(a))

print("\n===== COMPARISON =====")
print(a > 25)
print(a == 20)
print(np.any(a > 40))
print(np.all(a > 0))

print("\n===== RANDOM =====")
print(np.random.randint(1, 100, 5))

