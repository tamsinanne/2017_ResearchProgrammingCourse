# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:42:10 2017

@author: Tamsin PC
"""

def addition(a,b):
    """ adds two numbers of Fibonacci sequence"""
    return a+b

def FibNum(TotFib):
    """Calculates the fibonacci numbers """
    x=[1,1]

    for t in range(0,TotFib):
        newfib=addition(x[-1],x[-2])
        x.append(newfib)

    return x
    
def XPrint(TotFib):
    """Prints fibonacci numbers limiting the number of characters per line"""
    x=FibNum(TotFib)
    count1=0;    
    start1=0;
    start2=0;
    for i in x:
        count1=count1+len(str(i))+2
        if count1>=80:
            print(str(x[start1:start2]))
            count1=count1-80#           
            start1=start2
            
        start2=start2+1
    print(x[start1:(start2+1)])    