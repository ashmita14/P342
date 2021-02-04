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
check=boundary_dirichlet(f1,f2,t0,y0,yn,h,N,nm)
if check==True:
    print('Integration Successful.')
    #
else :
    print('Integration Not Successful.')
    #
