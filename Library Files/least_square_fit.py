# Least Square Fitting Code
import math
import lineareqns
import handling_files

def least_square(M,nm):
    n=len(M)
    x1=0
    x2=0
    y1=0
    x1y1=0
    for i in range(n):
        x1=x1+M[i][0]
        x2=x2+math.pow(M[i][0],2)
        y1=y1+M[i][1]
        x1y1=x1y1+(M[i][0]*M[i][1])
        #
    handling_files.append_file(nm, f'{n} {x1}\n')
    handling_files.append_file(nm,f'{x1} {x2}\n')
    Y=[0,0]
    Y[0]=y1
    Y[1]=x1y1
    A1=handling_files.read_matrix(nm)
    A=lineareqns.LU_decomposition(A1)
    Coef=lineareqns.forward_backward(A,Y)
    return(Coef)

def pearson(M):
    n=len(M)
    x1=0
    y1=0
    x1y1=0
    for i in range(n):
        x1 = x1 + M[i][0]
        y1 = y1 + M[i][1]
        #
    xavg=x1/n
    yavg=y1/n
    sxx=0
    syy=0
    sxy=0
    for i in range(n):
        sxx=sxx+math.pow((M[i][0]-xavg),2)
        syy=syy+math.pow((M[i][1]-yavg),2)
        sxy=sxy+(M[i][0]-xavg)*(M[i][1]-yavg)
        #
    r2=sxy*sxy/(sxx*syy)
    return(r2)
