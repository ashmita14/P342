#Question 3
import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

#reading matrix from file
M=read_matrix('q3data.txt')

#first fitting
name='q3(i)matrix elements store.txt'
file=open(name,'w')
C=least_square(M,name)
print('For First Fitting : \n')
print(f'Fit Function for (i) : \nw(t)={C[0]}+({C[1]})t')
#finding Pearson's r for first fitting
R2_i=pearson(M)
print(f'Value of Pearson`s r :\nr^2={R2_i}\nr={math.sqrt(R2_i)}\n')