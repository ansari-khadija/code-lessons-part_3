import numpy as np

# 2. Joining arrays
print("A. concatenate()")
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
result = np.concatenate((a, b))
print(result)

print("B. vstack()")
print(np.vstack((a, b)))

print("C. hstack()")
print(np.hstack((a, b)))

print("D. stack()")
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))