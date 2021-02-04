#Question 2
import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#defining all variables and the function to integrate
L=1
g=9.8
thtm=math.pi/4
a=math.sin(thtm/2)
T=lambda theta: 4*math.sqrt(L/g)*math.cos(theta/2)/(2*math.sqrt(1-math.pow(math.sin(theta/2),2))*math.sqrt(a*2-math.pow(math.sin(theta/2),2)))
nm='Integration data for question 2.txt'
file=open(nm,'w') #cleaning file

#defining upper limit, lower limit and N
up=math.pi/2
low=0
N=10

#calling function
I, h=simpson(T,low, up, N, nm)
print(f'Value of T obtained by Simpson method = {I}')
