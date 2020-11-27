#Question 2
#y''+y'=1-x 
#y(0)=2, y'(0)=1

import math
import sys

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#RK4
f1=lambda dy,y,x:dy
f2=lambda dy,y,x:1-x-dy
x0=0
y0=2
dy0=1
xmax=5
xmin=-5
for i in range(5):
    h=float(input('Enter value of h for eqn.\n'))
    N=int((xmax-xmin)/h)
    n=f'x vs y for eqn, h={h} N={N}'
    file=open(n, 'w') #refreshing file
    y1=RK4_double(f1,f2,x0,y0,dy0,-h,N,n) # for -ve x values
    y2=RK4_double(f1,f2,x0,y0,dy0,h,N,n) # for +ve x values
    #

    
    
    
    
################ OUTPUT ################
#Enter value of h for eqn.
#0.5
#Enter value of h for eqn.
#0.1
#Enter value of h for eqn.
#0.05
#Enter value of h for eqn.
#0.02
#Enter value of h for eqn.
#0.01
#
#Process finished with exit code 0
