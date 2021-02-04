#Question 1
import math
import sys
import os.path

sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *


f= lambda x: (x-5)*math.exp(x)+5
nm='Absolute Errors for q1.txt'
file=open(nm, 'w') #cleaning file
max=100 #setting max iterations to 100
a=int(input('Enter guess value of root.\n'))

h=6.626*math.pow(10,-34)
c=3*math.pow(10,8)
k=1.381*math.pow(10,-23)

root, check=newton_raphson(f, a,max,nm)
if check==True:
    print(f'Root value of x obtained at {root}.')
    b=(h*c)/(root*k)
    print(f'Value of Wein`s constant obtained = {b}')
    #
else :
    print('Root value of x not found.')
    #


    

    
########## OUTPUT ###############
#Enter guess value of root.
#5
#Root value of x obtained at 4.965114231744277.
#Value of Wein`s constant obtained = 0.002899010330738292
#
#Process finished with exit code 0
