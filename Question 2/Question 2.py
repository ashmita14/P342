# Question 2 - Monte Carlo Method for calculating volume of ellipsoid

import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

a=1.0
b=1.5
c=2.0
Vol=(4/3)*math.pi*a*b*c #theoritical volume
name_vol=f'N vs Volume obtained.txt' #file for storing N vs Volume
name_err=f'N vs Error.txt'
f1=open(name_vol, 'w')
f2=open(name_err,'w')
for i in range(12): #for 10 different values of N
    N = int(input('Enter N. \n'))
    name_p = f'Data Points for N={N}.txt'  # data file for points
    file = open(name_p, 'w')
    V=ellipsoidal(N, a, b, c, name_p)
    err=abs(Vol-V)/Vol
    append_file(name_vol, f'{N} {V}\n')
    append_file(name_err, f'{N} {err}\n')
    #


    
######################################## OUTPUT #######################################
#Enter N. 
#100
#Enter N. 
#500
#Enter N. 
#1000
#Enter N. 
#5000
#Enter N. 
#10000
#Enter N. 
#15000
#Enter N. 
#20000
#Enter N. 
#25000
#Enter N. 
#30000
#Enter N. 
#35000
#Enter N. 
#40000
#Enter N. 
#45000
#
#Process finished with exit code 0


