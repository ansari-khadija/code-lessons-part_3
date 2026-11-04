import numpy as np

print("===== zeros with dimensions =====")
# 1D 
a1 = np.zeros(5)
print(a1)
# 2D
a2 = np.zeros((2,3))
print(a2)

print("===== empty =====")
# 1D
b1 = np.round(np.empty(4),3)
print(b1)
# 2D
b2 = np.round(np.empty((2,3)),3)
print(b2)

print("===== sequence of numbers =====")
# 2-steps
c1 = np.arange(1, 5)
print(c1)
# 3-steps
c2 = np.arange(2,12,2)
print(c2)
c3 = np.arange(-1,12,2)
print(c3)

print("==== Create evenly spaced numbers ====")
d1 = np.linspace(1,20,2)
print(d1)
d2 = np.linspace(0,30,3)
print(d2)

print("=== an identity matrix ===")
e2 = np.eye(2)
print(e2)
e3 = np.eye(3,dtype=int)
print(e3)
print("===  Rectangular identity-style matrix ===")
e1 = np.eye(3,4,dtype=int)
print(e1)

print("=== array with a specific value ===")
f1 = np.full(4,88)
print(f1)
print("=== specific value with matrix ===")
f2= np.full((3,3),37)
print(f2)