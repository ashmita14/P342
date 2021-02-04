# Least Square Fitting Code
import math
import lineareqns
import handling_files

def least_square(M,n,nm):
    print(n)
    x1=0
    x2=0
    y1=0
    x1y1=0
    for i in range(n):
        x1=x1+M[0][i]
        x2=x2+math.pow(M[0][i],2)
        y1=y1+M[1][i]
        x1y1=xiyi+(M[0][i]*M[1][j])
        #
    handling_files.append_file(nm, f'{n} {x1}\n{x1} {x2}')
    Y=[0 0]
    Y[0]=y1
    Y[1]=x1y1
    A1=handling_files.read_matrix(nm)
    A=lineareqns.LU_decomposition(A1)
    Coef=lineareqns.forward_backward(A,Y)
    return(Coef)


