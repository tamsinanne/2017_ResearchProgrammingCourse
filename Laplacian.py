# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:15:55 2017

@author: Tamsin PC
"""

import numpy as np 
def Laplacian (indata,result,d):
    Sha=indata.shape
    for i in range(1,(Sha[0]-1)):
        for j in range(1,(Sha[1]-1)):
            result[i,j]=result[i,j]+(indata[(i-1),j]-2*indata[i,j]+indata[(i+1),j])/abs((d[0][i,j]-d[0][(i-1),j])*(d[0][i,j]-d[0][(i+1),j]))
            result[i,j]=result[i,j]+(indata[i,(j-1)]-2*indata[i,j]+indata[i,(j+1)])/abs((d[1][i,j]-d[1][i,(j-1)])*(d[1][i,j]-d[1][i,(j+1)]))
           
    return(result)        
        
    
    
    
    
A_Size=5;    
indata=np.random.rand(A_Size,A_Size)
x=np.linspace(0,1,A_Size)
y=np.linspace(0,1,A_Size)
d=np.meshgrid(x,y)
result=np.zeros([A_Size,A_Size])