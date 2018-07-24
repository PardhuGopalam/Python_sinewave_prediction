# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:18:47 2018

@author: Pardhu Gopalam
"""

import numpy as np
import random
import matplotlib.pyplot as plot

np.random.seed(245)
#k cannot be more than domain_len 
k = 100       #(<=10000)
domain_len = 10000
l = 10
mean = 0
var = 0.1
deg = 4
#l data sets on the domain each with k points with gaussioan noise added
d_space = np.linspace(0, 1, num = domain_len)
x_space = np.asarray(random.sample(list(d_space),k))
E =[]
D = np.zeros(l)
"""
for i in range(k):
    #x_space = np.asarray(random.sample(list(d_space),k))
    for j in range(l):
        E[j] = np.sin(2*np.pi * x_space) + np.random.normal(mean,np.sqrt(var),size=k)
"""
for j in range(l):
    random.seed(245)
    E.append(np.sin(2*np.pi * x_space) + np.random.normal(mean,np.sqrt(var),size=k))
D = np.asarray(E)

# 43 - 44 plots all the data sets. Comment them to ignore them
for i in range(l):
    plot.scatter(x_space,D[i])

    
'''  

'''
cum_x = []
cum_y = []
for i in range(l):
    for j in range(k):
        cum_x.append(x_space[j])
        cum_y.append(D[i][j])        
        

p = np.polyfit(cum_x, cum_y, deg, rcond=None, full=False, w=None, cov=False)        
def poly_func(x_space,p,deg,ith):
    y = 0
    for i in range(deg+1):
        y = y + ((p[i])*((x_space[ith])**(deg-i)))
        
    return(y)
y_predict1 = np.zeros(len(x_space))
for i in range(len(x_space)):
    y_predict1[i] = poly_func(x_space,p,deg,i)
    
y_predict = np.zeros(100)
t = np.arange(0.0, 1.0, 0.01)
for i in range(100):
    y_predict[i] = poly_func(t,p,deg,i)

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi *t)
line, = plot.plot(t, s, lw=4)
line, = plot.plot(t, y_predict, lw=2)
plot.ylim(-2,2)
plot.show()
    
    

    
    
        
        

