#Question 1
#Solve the system of equations :
#x_1+x_3+2x_4 = 6
#x_2-2x_3=-3
#x_1+2x_2-x_3=-2
#2x_1+x_2+3x_3-2x_4=0

#importing python file containing all functions
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib') #path of personal code library
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

print('The system of equations to solve : ')
print(f' x_{1}+x_{3}+2x_{4} = 6 \n x_{2}-2x_{3} = -3 \n x_{1}+2x_{2}-x_{3} = -2 \n 2x_{1}+x_{2}+3x_{3}-2x_{4} = 0')
name='A Matrix of Ques1.txt'
A=lineareqns.read_matrix(name)
print('The matrix A :')
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in A]))
A=LU_decomposition(A)
name='b Matrix of Ques1.txt'
B=lineareqns.read_vector(name)
print('The Matrix B : ')
print('\n'.join(['{0:6}'.format(item) for item in B]))
X=forward_backward(A,B)
#Final Computed Outputs
n=len(A)
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
#Solution X
print('The Solution Matrix X : ')
print('\n'.join(['{0:6}'.format(item) for item in X]))
print('Thus, we can write :')
for i in range(n):
    print(f'x_{i+1} = {X[i]}')

    
    
####### OUTPUT ######## (DIRECTLY COPY PASTED FROM RUN WINDOW)
#The system of equations to solve : 
# x_1+x_3+2x_4 = 6 
# x_2-2x_3 = -3 
# x_1+2x_2-x_3 = -2 
#2x_1+x_2+3x_3-2x_4 = 0
#The matrix A :
#     1     0     1     2
#     0     1    -2     0
#     1     2    -1     0
#     2     1     3    -2
#The Matrix B : 
#     6
#    -3
#    -2
#     0
#The Matrix L :
#  1.0  0.0  0.0  0.0
#
#  0.0  1.0  0.0  0.0
#
#  1.0  2.0  1.0  0.0
#
#  2.0  1.0  1.5  1.0
#
#The Matrix U :
#  1.0  0.0  1.0  2.0
#
#  0.0  1.0 -2.0  0.0
#
#  0.0  0.0  2.0 -2.0
#
#  0.0  0.0  0.0 -3.0
#
#The Solution Matrix X : 
#  1.0
#  -1.0
#   1.0
#   2.0
#Thus, we can write :
#x_1 = 1.0
#x_2 = -1.0
#x_3 = 1.0
#x_4 = 2.0
#
#Process finished with exit code 0
