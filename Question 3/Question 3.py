#Question 3
# y''=y'+1
# y(0)=1, y(1)=2(e-1)
# e=2.71828

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

    
    
 
####################### OUTPUT ############################

#Enter value of h for eqn.
#0.5
#Enter guess value of slope of curve at x=0.5 when y(0)=1
#0.8
#Guess value of slope again, greater than the previous guess.
#1.2
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#10000
#Integration is successful (for h=0.5).
#Enter value of h for eqn.
#0.1
#Enter guess value of slope of curve at x=0.1 when y(0)=1
#0.8
#Guess value of slope again, greater than the previous guess.
#1.1
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#10000
#Integration is successful (for h=0.1).
#Enter value of h for eqn.
#0.05
#Enter guess value of slope of curve at x=0.05 when y(0)=1
#0.9
#Guess value of slope again, greater than the previous guess.
#1.1
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#10000
#Integration is successful (for h=0.05).
#Enter value of h for eqn.
#0.02
#Enter guess value of slope of curve at x=0.02 when y(0)=1
#0.9
#Guess value of slope again, greater than the previous guess.
#1.0
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#10000
#Integration is successful (for h=0.02).
#Enter value of h for eqn.
#0.01
#Enter guess value of slope of curve at x=0.01 when y(0)=1
#0.9
#Guess value of slope again, greater than the previous guess.
#1.0
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#10000
#Integration is successful (for h=0.01).
#
#Process finished with exit code 0
