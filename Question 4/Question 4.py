#

import math
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
#importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

f=lambda x: 4/(1+math.pow(x,2))
nm_I='N vs Integration Value (Pi).txt'
nm_err='N vs Error.txt'
N=10 #starting value
#clearing  files before a fresh session
file1=open(nm_I, 'w')
file2=open(nm_err, 'w')
for i in range(1,3000+1): #
    I, err=montecarlo_uniform(f, 0, 1, N*i, nm_I, nm_err)
    #
