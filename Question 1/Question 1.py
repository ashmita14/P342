#Question 1

import math
import sys

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#FORWARD EULER'S METHOD
f1=lambda y,x:(y*math.log(y))/x
x10=2
y10=2.71828
N1=100
for i in range(5):
    h1=float(input('Enter value of h for eqn(1).\n'))
    n1=f'x vs y for eqn(1), h={h1} N={N1}'
    file=open(n1, 'w') #refreshing file
    forward_euler(f1,x10,y10,h1,N1,n1)
    #

f2=lambda y,x:6-(2*y)/x
x20=3
y20=1
N2=100
for i in range(5):
    h2=float(input('Enter value of h for eqn(2).\n'))
    n2=f'x vs y for eqn(2), h={h2} N={N2}'
    file=open(n2,'w')
    forward_euler(f2,x20,y20,h2,N2,n2)
    #


    
    
    
################ OUTPUT #####################
#Enter value of h for eqn(1).
#0.5
#Enter value of h for eqn(1).
#0.1
#Enter value of h for eqn(1).
#0.05
#Enter value of h for eqn(1).
#0.02
#Enter value of h for eqn(1).
#0.01
#Enter value of h for eqn(2).
#0.5
#Enter value of h for eqn(2).
#0.1
#Enter value of h for eqn(2).
#0.05
#Enter value of h for eqn(2).
#0.02
#Enter value of h for eqn(2).
#0.01
#
#Process finished with exit code 0

