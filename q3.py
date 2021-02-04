#Question 3
import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#reading matrix from file
M=read_matrix('q3data.txt')
name='q3matrix elements store.txt'
file=open(name,'w')
C=least_square(M,name)
print(C)