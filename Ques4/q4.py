#Question 4

import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#defining function
g=9.8
f1 = lambda dt, y, t: dt
f2 = lambda dt, y, t: -g
#setting initial values
t0=0
tn=5
y0=2
yn=45
#setting h (interval value) and N (number of iterations)
h=0.01
N=int((tn-t0)/h)

nm=f'q4 integration values.txt'
file=open(nm,'w')
#calling function and receiving slope at y(t=0)
slope,check=boundary_dirichlet(f1,f2,t0,y0,yn,h,N,nm)
if check==True:
    print('Integration Successful.')
    #
else :
    print('Integration Not Successful.')
    #
print(f'Launch Velocity (value of slope at y=2 and t=0) = {slope}m/s^2')





########## OUTPUT ##############
#Enter guess value of slope of curve at x=0.01 when y(0)=2
#30
#Guess value of slope again, greater than the previous guess.
#40
#Enter the upper limit on the number of iteration for finding the correct value of the slope.
#100
#Integration Successful.
#Launch Velocity (value of slope at y=2 and t=0) = 33.099999999999895m/s^2
#
#Process finished with exit code 0
