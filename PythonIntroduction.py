# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:17:44 2017

@author: Tamsin PC
"""

lista=[1,2,3]
listb="I am a string"
listc=[1,"a",lambda x:x+1]
lista[2]=42
print(listc[2](3))

dictionary={"key1":"value1","key2": "value2"}
loci={(1,2): "person 1", (2,42): "person 2", (32,8): "person 3"}
for k,v in dictionary.items():
    print('key "{k}" has value "{v}"'.format(k=k,v=v))
coord=(2,42)
print("It is {cmp} that there is a person at {coord}.".format(cmp=coord in loci.keys(),coord=coord))
b=(1,42)
print("Equality of {a} and {b} evalues to {val}.".format(a=coord,b=b,val=b==coord))

import numpy
skewed=numpy.random.random((2,3,4))
array=numpy.arange(0,27)
array=array.reshape(3,3,3)

import scipy 
import scipy.special
scipy.special.kn(2,array)
import scipy.fftpack
scipy.fftpack.fftn(array)

def findzeros(a,b,c):
    '''Find the real root(s) fo "a x^2 +bx+c". 
    >>> findzeros(1,4,3)
    (-1.0,-3.0)
    >>> findzeros(1,-2,-3)
    (1.0,-3.0)
    '''
    
    root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return(root1,root2)

import urllib
import urllib.request
def get_url(url='http://www.cam.ac.uk/'):
    data=[]
    with urllib.request.urlopen(url) as response:
        charset = response.headers.get_content_charset()
        for line in response:
            data.append(link.decode(charset))
    return data
    
def multiply(*args):
    res=1
    for a in args:
        res=res*a
    return res
    
def many_args(a,b,c=42,d=0,*e,**f):
    print("a= "+str(a))
    print("b= "+str(b))
    print("c= "+str(c))
    print("d= "+str(d))
    for i,E in enumerate(e): print("e[{idx}] = ".format(idx=i)+str(E))
    for F in f: print("f[{key}]= ".format(key=F) + str(f[F]))
        
    