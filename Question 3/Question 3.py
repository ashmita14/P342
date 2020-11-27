#Question 3

import math
import sys

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#Boundary Value Problem
f1=lambda dy,y,x:dy
f2=lambda dy,y,x:dy+1
x0=0
y0=1
xn=1
yn=2*(2.71828-1)
for i in range(5):
    h=float(input('Enter value of h for eqn.\n'))
    N=int((xn-x0)/h)
    n=f'x vs y for eqn, h={h} N={N}'
    file=open(n, 'w') #refreshing file
    T=boundary_dirichlet(f1,f2,x0,y0,yn,h,N,n)
    if(T==True): print(f'Integration is successful (for h={h}).')
    else: print(f'Integration unsuccessful (for h={h}).')
    #
