#Check if the given atrixhas an inverse. If yes, find it.
# 0 2 8 6
# 0 0 1 2
# 0 1 0 1
# 3 7 1 0

#Procedure opted by me for finding the inverse : A*inv(A)=I
# I have solved the equations A*a_i = b_i,
# where a_i and b_i are columns of Inverse A matrix and Identity matrix respectively

#importing python file containing all functions
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
import lineareqns

def LU_decomposition(x): #Using Crout's method
    n=len(x) #no. of rows
    m=len(x[0]) #no. of columns
    for j in range(m): #for rows
        for i in range(n): #for columns
            if i<j: #upper-triangular ==> elements of U
                for k in range(i): #loops from 0 to i-1
                    x[i][j]=float(x[i][j]-x[i][k]*x[k][j])
                    #
                #
            if i==j: #diagonal elements of U
                for k in range(i):
                    x[j][j]=float(x[j][j]-x[j][k]*x[k][j])
                    #
                #
            if i>j: #lower diagonal ==> elements of L
                for k in range(j): #loops from 0 to j-1
                    x[i][j]=float(x[i][j]-x[i][k]*x[k][j])
                    #
                x[i][j]=x[i][j]/float(x[j][j])
            #
        #
    return(x)
def forward_backward(a,b):
    # we solve (LU)X=b
    # Let UX=Y;
    # First we solve LY=b and then UX=Y
    n=len(a) #number of rows
    m=len(a[0]) #number of columns
    #we can just modify b for both X and Y because each element is used only once before modifiation

    #FORWARD SUBSTITUTION : LY=b
    for i in range(n):
        for j in range(i): # i>j (as L is lower triangular)
            b[i]=float(b[i]-a[i][j]*b[j])
            #
        #
    #BACKWARD SUBSTITUTION : UX=Y
    for i in range(3,-1,-1): #i goes in decreasing order, from 3 to 0
        for j in range(i+1,n): # i<j(as U is upper triangular)
            b[i]=b[i]-a[i][j]*b[j]
            #
        b[i]=float(b[i])/a[i][i]
        #
    return(b)

name='A Matrix of Ques2.txt'
A=lineareqns.read_matrix(name)
print('The Matrix A :')
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in A]))
n=len(A)
I=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    I[i][i]=1
    #
#Augmenting A with identity matrix for partial pivoting
Aug=[[0 for j in range(2*n)] for i in range(n)]
for i in range(n):
    for j in range(2*n):
        if j<n: Aug[i][j]=A[i][j]
        else: Aug[i][j]=I[i][j-n]
        #
    #
Aug=lineareqns.partial_pivot(Aug)
print('Augmented Matrix after partial pivot :')
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in Aug]))
#Extracting A from Augmented matrix after partial pivot
for i in range(n):
    for j in range(n):
        A[i][j]=Aug[i][j]
        #
    #
A=LU_decomposition(A)
print('\nAfter LU Decomposition : ')
#Matrix L
print('The Matrix L :')
for i in range(n):
    for j in range(n):
        if i>j:
            print("{0:5}".format(float(A[i][j])), end='')
            #
        if i==j:
            print("{0:5}".format(1.0), end='')
            #
        if i<j:
            print("{0:5}".format(0.0), end='')
            #
        #
    print('\n')
    #
#Matrix U
print('The Matrix U :')
for i in range(n):
    for j in range(n):
        if i<=j:
            print("{0:5}".format(float(A[i][j])), end='')
            #
        if i>j:
            print("{0:5}".format(0.0), end='')
            #
        #
    print('\n')
    #

#finding determinant
det=1
for i in range(n):
    det=det*A[i][i]
    #
if det!=0:
    print(f'The value of determinant is = {det} \n As it is not equal to zero, inverse of matrix A exists.')
else: print('The value of determinant of A is zero, thus inverse does not exist.')
inv_A=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    b=[0 for i in range(n)]
    #extracting i'th column and passing on to forward backward substitution function
    for j in range(n):
        b[j]=Aug[j][i+n]
        #
    b=forward_backward(A,b)
    #storing result (i'th coumn of A inverse)
    for j in range(n):
        inv_A[j][i]=b[j]
        #
    #
print('A Inverse :')
print('\n'.join([''.join(['{0:8}'.format(round(item, 3)) for item in row])for row in inv_A]))



########## OUTPUT ########## (COPY PASTED DIRECTLY FROM RUN WINDOW)
#The Matrix A :
#     0     2     8     6
#     0     0     1     2
#     0     1     0     1
#     3     7     1     0
#Augmented Matrix after partial pivot :
#     3     7     1     0     0     0     0     1
#     0     2     8     6     1     0     0     0
#     0     0     1     2     0     1     0     0
#     0     1     0     1     0     0     1     0
#
#After LU Decomposition : 
#The Matrix L :
#  1.0  0.0  0.0  0.0
#
#  0.0  1.0  0.0  0.0
#
#  0.0  0.0  1.0  0.0
#
#  0.0  0.5 -4.0  1.0
#
#The Matrix U :
#  3.0  7.0  1.0  0.0
#
#  0.0  2.0  8.0  6.0
#
#  0.0  0.0  1.0  2.0
#
#  0.0  0.0  0.0  6.0
#
#The value of determinant is = 36.0 
# As it is not equal to zero, inverse of matrix A exists.
#A Inverse :
#   -0.25   1.667  -1.833   0.333
#   0.083  -0.667   0.833     0.0
#   0.167  -0.333  -0.333     0.0
#  -0.083   0.667   0.167     0.0
#
#Process finished with exit code 0

