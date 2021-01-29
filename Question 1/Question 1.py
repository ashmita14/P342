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

    append_file(nm1, f'{math.sqrt(N)} {Rrms}\n')

#######################################




######################### OUTPUT #################################
#Enter value of N (no. of steps)
#250
#For N=250
#RMS Value of Radial Distance (R) = 15.229181480111528
#Average Value of displacement along x-axis = -2.1421040236083595
#Average Value of displacement along y axis =-0.37145133370373196
#
#Enter value of N (no. of steps)
#400
#For N=400
#RMS Value of Radial Distance (R) = 21.344343473468083
#Average Value of displacement along x-axis = 0.43618998122651775
#Average Value of displacement along y axis =0.8259966782170534
#
#Enter value of N (no. of steps)
#500
#For N=500
#RMS Value of Radial Distance (R) = 21.86996340091884
#Average Value of displacement along x-axis = -2.1346444774009874
#Average Value of displacement along y axis =-2.735873831597171
#
#Enter value of N (no. of steps)
#750
#For N=750
#RMS Value of Radial Distance (R) = 25.667787649772517
#Average Value of displacement along x-axis = -1.0307460071647516
#Average Value of displacement along y axis =0.9538076454593591
#
#Enter value of N (no. of steps)
#1000
#For N=1000
#RMS Value of Radial Distance (R) = 31.042902564091282
#Average Value of displacement along x-axis = -2.3153947887926063
#Average Value of displacement along y axis =-0.4602628273242385
#
#
#Process finished with exit code 0

