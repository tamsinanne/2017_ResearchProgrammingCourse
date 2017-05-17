# -*- coding: utf-8 -*- 
"""Created on Wed May  3 15:51:32 2017 """
import matplotlib.pyplot as plt

def SquareNum(m):
    return([i**2 for i in m])
    
n=range(10)
n1=SquareNum(n)
plt.plot(n,n1,'--r+')
plt.show()