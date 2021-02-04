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
Ci=least_square(M,name)
print('For First Fitting : \n')
print(f'Fit Function for (i) : \nw(t)={Ci[0]}+({Ci[1]})t\n')
#finding Pearson's r for first fitting
R2_i=pearson(M)
print(f'Value of Pearson`s r :\nr^2={R2_i}\nr={math.sqrt(R2_i)}\n')

#second fitting
n=len(M)
m=len(M[0])
N=[[0 for j in range(m)] for i in range(n)]
#taking ln of each angular velocity value
for i in range(n):
    N[i][0]=M[i][0]
    N[i][1]=math.log(M[i][1])
    #
name1='q3(ii)matrix elements store.txt'
file1=open(name1,'w')
Cii=least_square(N,name1) #calling least square function
print('For Second Fitting : \n')
print(f'Fit Function for (ii) : \nln w(t)={Cii[0]}+({Cii[1]})t\nw(t)=exp({Cii[0]}+({Cii[1]})t)\n')
#finding Pearson's r for first fitting
R2_ii=pearson(N)
print(f'Value of Pearson`s r :\nr^2={R2_ii}\nr={math.sqrt(R2_ii)}\n')






########## OUTPUT #########################
#For First Fitting : 
#
#Fit Function for (i) : 
#w(t)=2.029102564102564+(-0.47470862470862485)t
#
#Value of Pearson`s r :
#r^2=0.9705318844905291
#r=0.9851557666128383
#
#For Second Fitting :
#
#Fit Function for (ii) : 
#ln w(t)=0.7902775293458721+(-0.39559617454855667)t
#w(t)=exp(0.7902775293458721+(-0.39559617454855667)t)
#
#Value of Pearson`s r :
#r^2=0.9982366554936271
#r=0.9991179387307721
#
#
#Process finished with exit code 0
