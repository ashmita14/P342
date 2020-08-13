#Question 3

#importing array
import array as arr

#Opening and reading Matrix M from file
f = open('M.txt' , 'r')
M = [[int(num) for num in line.split(',')] for line in f]
print("Matrix M : ")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in M]))
#Opening and reading Matrix N from file
g = open('N.txt', 'r')
N = [[int(num) for num in line.split(',')] for line in g]
print("Matrix N : ")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in N]))
#Array A
A=arr.array('i', [3,8,7]) #Same as Question 2

cross="\u2716" #cross symbol

#M cross A
MA=[0]*3
t1=0
for i in range(3):
    for j in range(3):
        t1=MA[i]
        MA[i]=t1+M[i][j]*A[j]
    #
print("Matrix M", cross, " A : ")
print('\n'.join(['{:6}'.format(item) for item in MA]))

#M cross N
MN=[[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            t2=MN[i][j]
            MN[i][j]=t2+M[i][k]*N[k][j]
        #
    #
print("Matrix M",  cross, " N : ")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in MN]))