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
# N=250
N1=250
R_250 = [0 for i in range(n)] #for storing final radial distance
X_250 = [0 for i in range(n)] #for storing final x value
Y_250 = [0 for i in range(n)] #for storing final y value
path_250= 'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N=250'
for i in range(n):
    nm_250=f'Walk {i+1} of steps N={N1}.txt'
    name_250=os.path.join(path_250,nm_250)
    file=open(name_250, 'w') #clearing file before
    #generating random walk, each step should be some value between -1 to 1
    R_250[i], X_250[i], Y_250[i]=walk(N1, name_250)
    #
#Rrms and averages
Rrms_250, avgx_250, avgy_250 = averages(n, R_250, X_250, Y_250)
#OUTPUT for N=250
print(f'For N={N1}\nRMS Value of Radial Distance (R) = {Rrms_250}\nAverage Value of displacement along x-axis = {avgx_250}\nAverage Value of displacement along y axis ={avgy_250}\n')

append_file(nm1, f'{N1} {Rrms_250}\n')
#######################################

#N=300
N2=300
R_300 = [0 for i in range(n)] #for storing final radial distance
X_300 = [0 for i in range(n)] #for storing final x value
Y_300 = [0 for i in range(n)] #for storing final y value
path_300= 'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N=300'
for i in range(n):
    nm_300=f'Walk {i+1} of steps N={N2}.txt'
    name_300=os.path.join(path_300,nm_300)
    file=open(name_300, 'w') #clearing file before
    #generating random walk, each step should be some value between -1 to 1
    R_300[i], X_300[i], Y_300[i]=walk(N2, name_300)
    #
#Rrms and averages
Rrms_300, avgx_300, avgy_300 = averages(n, R_300, X_300, Y_300)
#OUTPUT for N=300
print(f'For N={N2}\nRMS Value of Radial Distance (R) = {Rrms_300}\nAverage Value of displacement along x-axis = {avgx_300}\nAverage Value of displacement along y axis ={avgy_300}\n')

append_file(nm1, f'{N2} {Rrms_300}\n')
###########################################################

# N=350
N3=350
R_350 = [0 for i in range(n)] #for storing final radial distance
X_350 = [0 for i in range(n)] #for storing final x value
Y_350 = [0 for i in range(n)] #for storing final y value
path_350= 'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N=350'
for i in range(n):
    nm_350=f'Walk {i+1} of steps N={N3}.txt'
    name_350=os.path.join(path_350,nm_350)
    file=open(name_350, 'w') #clearing file before
    #generating random walk, each step should be some value between -1 to 1
    R_350[i], X_350[i], Y_350[i]=walk(N3, name_350)
    #
#Rrms and averages
Rrms_350, avgx_350, avgy_350 = averages(n, R_350, X_350, Y_350)
#OUTPUT for N=350
print(f'For N={N3}\nRMS Value of Radial Distance (R) = {Rrms_350}\nAverage Value of displacement along x-axis = {avgx_350}\nAverage Value of displacement along y axis ={avgy_350}\n')

append_file(nm1, f'{N3} {Rrms_350}\n')
#################################################################

# N=400
N4=400
R_400 = [0 for i in range(n)] #for storing final radial distance
X_400 = [0 for i in range(n)] #for storing final x value
Y_400 = [0 for i in range(n)] #for storing final y value
path_400= 'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N=400'
for i in range(n):
    nm_400=f'Walk {i+1} of steps N={N4}.txt'
    name_400=os.path.join(path_400,nm_400)
    file=open(name_400, 'w') #clearing file before
    #generating random walk, each step should be some value between -1 to 1
    R_400[i], X_400[i], Y_400[i]=walk(N4, name_400)
    #
#Rrms and averages
Rrms_400, avgx_400, avgy_400 = averages(n, R_400, X_400, Y_400)
#OUTPUT for N=400
print(f'For N={N4}\nRMS Value of Radial Distance (R) = {Rrms_400}\nAverage Value of displacement along x-axis = {avgx_400}\nAverage Value of displacement along y axis ={avgy_400}\n')

append_file(nm1, f'{N4} {Rrms_400}\n')
#################################################################

# N=450
N5=450
R_450 = [0 for i in range(n)] #for storing final radial distance
X_450 = [0 for i in range(n)] #for storing final x value
Y_450 = [0 for i in range(n)] #for storing final y value
path_450= 'C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/Assignment 8/Question 1/N=450'
for i in range(n):
    nm_450=f'Walk {i+1} of steps N={N5}.txt'
    name_450=os.path.join(path_450,nm_450)
    file=open(name_450, 'w') #clearing file before
    #generating random walk, each step should be some value between -1 to 1
    R_450[i], X_450[i], Y_450[i]=walk(N5, name_450)
    #
#Rrms and averages
Rrms_450, avgx_450, avgy_450 = averages(n, R_450, X_450, Y_450)
#OUTPUT for N=450
print(f'For N={N5}\nRMS Value of Radial Distance (R) = {Rrms_450}\nAverage Value of displacement along x-axis = {avgx_450}\nAverage Value of displacement along y axis ={avgy_450}\n')

append_file(nm1, f'{N5} {Rrms_450}\n')