import numpy as np

print("=== dtype in numpy ===")
a = np.array([10,20,30,40])
a1 = np.array([1.1,2.2,3.3,4.4])
a2 = np.array(["cat","dog","mouse","birds"])
a3 = np.array([True,True,False,False])
a4= np.array(["22","33","44","66"])
print(a,"--->",a.dtype)
print(a1,"--->",a1.dtype)
print(a2,"--->",a2.dtype)
print(a3,"--->",a3.dtype)

print("=== Convert data types ===")
b = a.astype(float)
print(a,":",a.dtype,"--->",b,":",b.dtype)
b1 = a1.astype(int)
print(a1,":",a1.dtype,"--->",b1,":",b1.dtype)
b2 = a4.astype(int)
print(a4,":",a4.dtype,"--->",b2,":",b2.dtype)
b3 = a.astype(str)
print(a,":",a.dtype,"--->",b3,":",b3.dtype)

print("=== Change array dimensions ===")
c = a.reshape(2,2)
print("Convert 1D into 2D :",c)
c1 = np.array([11,12,13,14,15,16])
print(c1.reshape(2,3))
c2= np.array([11,12,13,14,15,16])
print(c2.reshape(3,2))
c3= np.arange(12)
c4= c3.reshape(3, -1)
print("Reshape by arange method:",c4)

print("===  Convert multidimensional arrays into 1D ===")
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(d)
d1= np.array([[1, 2], [3, 4]])
d2 = d1.flatten()
d2[0] = 100
print("Original:", d1)
print("Flattened:", d2)

print("=== Change array size ===")
e1= np.array([1, 2, 3, 4])
e2 = np.resize(e1 , (2, 3))
print(e2)

print("=== Change rows into column ===")
f = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
f2 = f.transpose()
print(f2)