import numpy as np
import matplotlib.pyplot as plt



#
a = [[11, 12, 13], [21, 22, 23],[31, 32, 33]]
# a = [[[1, 2]]]
print(a)
print("\n-------------------\n")

# mengubah list ke numpy array
A = np.array(a)
print(A)
print("\n-------------------\n")

# print dimensi array
print(A.ndim)
print("\n-------------------\n")

# print shape nya terluar - terdalam
print(A.shape)
print("\n-------------------\n")

# print size : hasil perkalian dimensinya / jumlah isinya
print(A.size)
print("\n-------------------\n")

# access index 2nd row 3rd col
# bisa satu persatu
print(A[1,2])
print(A[1][2])
print("\n-------------------\n")

# slicing
print(A[0][0:2])
print(A[0:2,2])
print("\n-------------------\n")

# operation +
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
Z = X + Y
print(Z)
print("\n-------------------\n")

# operation * number
Y = np.array([[2, 1], [1, 2]])
Z = 2 * Y
print(Z)
print("\n-------------------\n")

# operation * 2 numpy 2d array (per lokasi)
Y = np.array([[2, 1], [1, 2]])
X = np.array([[1, 0], [0, 1]])
Z = X * Y
print(Z)
print("\n-------------------\n")

# perkalian dot 2D array
# 2 x 3 || 3 x 2 |=| 2 x 2
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
Z = np.dot(A,B)
print(Z)
print(np.sin(Z))
print("\n-------------------\n")

# Transpose
C = np.array([[1,1],[2,2],[3,3]])
print(C.T)
print("\n-------------------\n")

#
# print("\n-------------------\n")

#
# print("\n-------------------\n")
