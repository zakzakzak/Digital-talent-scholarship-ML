from __future__ import print_function
import time
import sys
import numpy as np

import matplotlib.pyplot as plt


# fungsi gambar plot
def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    # plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    # plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    # plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    # plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    # plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

#
a = ["0", 1, "two", "3", 4]
print(a)
print("\n-------------------\n")



#
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print("\n-------------------\n")

#
import numpy as np
print("\n-------------------\n")

#
a = np.array([0, 1, 2, 3, 4])
print(a)
print("\n-------------------\n")

#
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print("\n-------------------\n")

#
print(type(a))
print(a.dtype)
print("\n-------------------\n")

#
b = np.array([3.1, 11.02, 6.2, 213.2, 5.4])
print(type(b))
print(b.dtype)
print("\n-------------------\n")

# assign index
c = np.array([20, 1, 2, 3, 4])
print(c)
c[0] = 100
print(c)
print("\n-------------------\n")

# slicing and assign slicing
d = c[1:4]
print(d)
c[3:5] = 300, 400
print(c)
print("\n-------------------\n")

# assign with list (per index) dari c
select = [0, 2, 3]
d = c[select]
print(d)
c[select] = 100000
print(c)
print("\n-------------------\n")

#
a = np.array([0, 1, 2, 3, 4])
print(a.size)
print(a.shape)
print("\n-------------------\n")


# mean, std
a = np.array([1, -1, 1, -1])
mean = a.mean()
print(mean)
standard_deviation=a.std()
print(standard_deviation)
print("\n-------------------\n")


# max, min
b = np.array([-1, 2, 3, 4, 5])
print(b.max())
print(b.min())
print("\n-------------------\n")


# operation jumlah per lokasi
u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
print(z)
print("\n-------------------\n")


# Plotvec1
Plotvec1(u, z, v)
plt.show()
print("\n-------------------\n")

# operasi * array ultiplication
y = np.array([1, 2])
z = 2 * y
print(z)
print("\n-------------------\n")

# product of 2 np array kali setiap posisi
# dot product : dikali semua posisi lalu ditambah
u = np.array([1, 2])
v = np.array([3, 2])
z = u * v
print(z)
print(np.dot(u, v))
print("\n-------------------\n")

# menambah 1 setiap isi indexnya
u = np.array([1, 2, 3, -1])
print(u+1)
print("\n-------------------\n")

# memanggil pi
print(np.pi)
print("\n-------------------\n")

#
x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)
print(y)
print("\n-------------------\n")

# linspace (mulai, sampai, sebanyak berapa?) num = spaced numbers
print(np.linspace(-2, 2, num=5))
print("\n-------------------\n")

#
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
print("\n-------------------\n")

#

u = np.array([1, 0])
v = np.array([0, 1])
print("1.", (u-v) )

z = np.array([2, 4])
print("2.", z*-2)

a = np.array([1,2,3,4,5])
b = np.array([1,0,1,0,1])
print("3.", a*b)

a = [-1,1]
b = [1,1]
print("4.", np.dot(a,b))
Plotvec2(a,b)
plt.show()
print("\n-------------------\n")



















# END
