# Question 1a
# log(x)-sin(x)=0

import math
#importing python file containing all functions
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib') #path of personal code library
import non_lineareqns

#########################################################################

f=lambda x: math.log(x)-math.sin(x) #given function
#bracketing the given function
a, b, chk_brac = non_lineareqns.bracketing(f, 1.5, 2.5, 10)
if chk_brac==True:
    print(f'Bracketing Complete. \na={a} and b={b}')
else: print("Bracketing not complete")

##########################################################################

#bisection method
name_bi='Absolute Error Bisection (1a).txt'
file=open(name_bi, 'w') #'w' ==> write #clearing up contents of file to make fresh entries
root_bi, chk_bisec = non_lineareqns.bisection_1(f, a, b, 100, name_bi)
if chk_bisec==True:
    print(f'Bisection method successful in given number of iterations.\nRoot = {round(root_bi, 3)}')
else: print("Roots not found in maximum allowed iterations in Bisection.")

###############################################################################

#regula falsi method
name_rf='Absolute Error Regula Falsi (1a).txt'
file=open(name_rf, 'w') #'w' ==> write #clearing up contents of file to make fresh entries
root_rf, chk_rf=non_lineareqns.regula_falsi(f, a, b, 100, name_rf)
if chk_rf==True:
    print(f'Regular Falsi method successful in given number of iterations.\nRoot = {round(root_rf, 3)}')
else: print("Roots not found in maximum allowed iterations in Regular Falsi.")

###########################################################################

#Newtown raphson method
name_nr='Absolute Errors Newton Raphson (1a).txt'
file=open(name_nr, 'w') #'w' ==> write, clearing up file contents before making new entry
root_nr, chk_nr=non_lineareqns.newton_raphson(f, 1.5, 100, name_nr)
if chk_nr==True:
    print(f'Newton Raphson method successful in given number of iterations. \nRoot = {round(root_nr, 3)}')
else: print("Roots not found in maximum allowed iterations in Newton Raphson.")

#Giving user the option to display file containing value of errors with convergence
read=input('Type Y if you wish to see files of Absolute Errors. Else, type N.\n')
if read=='Y':
    choose=input('Type BI for viewing Absolute Errors of Bisection Method.\n'
                 'Type RF for viewing Absolute Errors of Regular falsi Method.\n'
                 'Type NR for viewing Absolute Errors of Newton Raphson Method.\n'
                 'Type ALL for viewing all.\n')
    if choose=='BI':
        print('Iteration Number vs. Absolute Error (Bisection Method)')
        non_lineareqns.print_file(name_bi)
    elif choose=='RF':
        print('Iteration Number vs. Absolute Error (Regula Falsi Method)')
        non_lineareqns.print_file(name_rf)
    elif choose =='NR':
        print('Iteration Number vs. Absolute Error (Newton Raphson Method)')
        non_lineareqns.print_file(name_nr)
    elif choose =='ALL':
        print('Iteration Number vs. Absolute Error (Bisection Method)')
        non_lineareqns.print_file(name_bi)
        print('Iteration Number vs. Absolute Error (Regula Falsi Method)')
        non_lineareqns.print_file(name_rf)
        print('Iteration Number vs. Absolute Error (Newton Raphson Method)')
        non_lineareqns.print_file(name_nr)
    else:
        print('Invalid Choice.\n')

