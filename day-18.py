list1=[1,2,3,4,5]

(list1) * (10)

list1=[0]*10

list2=[]

for i in list1:
    list2.append(i*10)
    
    
[i * 10 for i in list1]  #list comprehension

import numpy as n

y=n.array(list1)

y.shape
y.ndim

x=10 # scaler value 0 dimension

x=n.array(x)

x1=[10]  #vector value 1D

x1=n.array(x1)


x2=[[10]]  #vector 2D

x2=n.array(x2)

x3=[[[10]]] #vector 2D

x3=n.array(x3)

list1=[1,2,3,4,5,6,7,8,9]

x4=n.array(list1)
x4.reshape(3,3)

x4=n.arange(5,dtype= n.int32)  #to change storage space from int64 to int32 example dataloss may occur

n.ones((3,4), dtype=n.int8)  #float data type converting to integer
n.zeros((4,5))  #float data type

import matplotlib.pyplot as m

x=[1,2,3,4,5]
y=[1,2,3,4,5]


#m.scatter(x,y)
#m.plot(x,y)

x=n.arange(20)
y=[item**3 for item in x]
m.scatter(x,y)
m.plot(x,y)
