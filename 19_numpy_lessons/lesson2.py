from numpy import *

print("===== 1D Array =====")
# 1D Array
a = array([10, 20, 30, 40, 50])
print(a)
print(type(a))

print("===== 2D Array =====")
# 2D Array
b = array([[1, 2, 3], [4, 5, 6]])
print(b)
print(type(b))

print("===== 3D Array =====")
# 3D Array
c = array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)
print(type(c))

print("===== Array Properties =====")
# array properties
print("Dimensions:", b.ndim)
print("Size:", b.size)
print("Shape:", b.shape)
print("Data Type:", b.dtype)
print("Item Size:", b.itemsize)
print("Total Bytes:", b.nbytes)