#Question 1 - Random Walk in Two Dimension

import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

n=100
nm1=f'Rrms vs sqrt(N).txt'
g=open(nm1, 'w')

for j in range(5):
    N = int(input('Enter value of N (no. of steps)\n'))
    R = [0 for i in range(n)]  # for storing final radial distance
    X = [0 for i in range(n)]  # for storing final x value
    Y = [0 for i in range(n)]  # for storing final y value
    path = f'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N={N}'
    for i in range(n):
        nm = f'Walk {i + 1} of steps N={N}.txt'
        name = os.path.join(path, nm)
        file = open(name, 'w')  # clearing file before
        # generating random walk, each step should be some value between -1 to 1
        R[i], X[i], Y[i] = walk(N, name)
        #
    # Rrms and averages
    Rrms, avgx, avgy = averages(n, R, X, Y)
    # OUTPUT for N
    print(
        f'For N={N}\nRMS Value of Radial Distance (R) = {Rrms}\nAverage Value of displacement along x-axis = {avgx}\nAverage Value of displacement along y axis ={avgy}\n')

    append_file(nm1, f'{N} {Rrms}\n')

#######################################
