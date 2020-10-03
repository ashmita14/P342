
import math
#importing python file containing all functions
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib') #path of personal code library
import non_lineareqns

f=lambda x: pow(x, 4)-3*pow(x, 3)-7*pow(x, 2)+27*x-18 #given eqaution
n=4 #order of equations
X=[-18, 27, -7, -3, 1] #array of coefficients, from a_0 to a_4
for i in range(n): #calling laguerre and deflation function, repeatedly
    trial=float(input(f'Enter trial value {i+1} of root.'))
    root, chk=non_lineareqns.laguerre(f, trial, 100, n)
    if chk==True:
        print(f'Root {i+1} = {round(root,3)}')
        f, X, rm = non_lineareqns.deflation(X, root, n-i)
        #
    else:
        print(f'Root {i+1} not obtained in maximum allowed iterations.')

