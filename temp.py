

a=3
b=4
c=a+b
print(c)
import pandas as pd
import numpy as np
mystring="hello world"
len(mystring)
mystring[1]
mystring[0]
mystring[5:10]
mystring[:7]
mystring[3:]
example=mystring[:5]


#tupple

mytuple=(11,12,13)
mytuple+=(44,)

import numpy as np
np.mean(mytuple)
np.median(mytuple)
tuple=sorted(mytuple)


#definition

def area_volume_of_cube(sidelength):
    area=6*sidelength*sidelength
    volume=sidelength*sidelength*sidelength
    return area,volume
area_volume_of_cube(6)

def simple_interest(principal,years,rate):
    si=(principal*years*rate)/100
    return si
simple_interest(1000,2,0.10)

def compound_interest(principal,rate,years):
    ci=principal*(pow((1+rate/100),years))
    return ci
compound_interest(1000,0.10,2)

#tuple

mytuple=(1,3,4,True,"hello")


#dictionaries

numerictoroman={1:"i",2:"ii",3:"iii",4:"iv",5:"v"}
numerictoroman[2]
numerictoroman[6]="vi"
numerictoroman[3]="iiii"

ages={"vishnu":24,"muruga":25}
saved=ages
ages["vishnu"]=25

numerictoroman.items()
ages.keys()
ages.values() 

ages.pop("vishnu")  
numerictoroman.popitem()

#aliases

a=[1,2,True,"eat"] 
b=a
a[1]=3

cset={11,11,22}
cset
aset={11,22,33}
bset=aset

aset={11,22,33}
bset={11,22,33,44}
aset|bset
aset&bset

aset={11,22,33}
bset={12,23,33}
aset-bset
aset^bset

#numpy

import numpy as np
data1=[[1,2,3,4],[6,7,8,9]]
ar1=np.array(data1)
ar1.ndim
ar1.shape
np.zeros((3,4))
np.random.randn(3,5)
np.arange(27).reshape(3,3,3)
arr=np.arange(15)
arr[4:7]
arr=np.random.randn(3,5)
arr_tarns=arr.T
random_array=np.dot(arr,arr_tarns)
arr1=np.arange(6).reshape(2,3)
arr2=np.arange(6).reshape(3,2)
arr_random=np.dot(arr1,arr2)

arr3=[1,2,3]
arr4=[4,1,2]
np.greater_equal(arr3,arr4)

x1=[True,True,False,True]
x2=[True,False,False,False]
np.logical_and(x1,x2)
np.mean(arr3)

arr5=np.array([[1,2,3],[4,5,6]])

x=np.random.random(10)
y=np.random.random(10)
z=np.random.random(10)
apple=np.array(zip(x,y,z))

vishnu=np.array([[1,2,3],[4,5,6]])
muruga=np.zeros((2,1))
np.append(vishnu,muruga,axis=1)