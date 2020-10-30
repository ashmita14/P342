#

import math
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
#importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

f=lambda x: x/(x+1)
name_mid_5='Midpoint(2) N=5.txt'
file=open(name_mid_5, 'w')
I_mid5, h_mid5=midpoint(f, 1, 3, 5, name_mid_5)

name_mid_10='Midpoint(2) N=10.txt'
file=open(name_mid_10, 'w')
I_mid10, h_mid10=midpoint(f, 1, 3, 10, name_mid_10)

name_mid_25='Midpoint(2) N=25.txt'
file=open(name_mid_10, 'w')
I_mid25, h_mid25=midpoint(f, 1, 3, 25, name_mid_25)

name_trap_5='Trapezoidal(2) N=5.txt'
file=open(name_trap_5, 'w')
I_trap5, h_trap5 =trapezoidal(f, 1, 3, 5, name_trap_5)

name_trap_10='Trapezoidal(2) N=10.txt'
file=open(name_trap_10, 'w')
I_trap10, h_trap10 =trapezoidal(f, 1, 3, 10, name_trap_10)

name_trap_25='Trapezoidal(2) N=25.txt'
file=open(name_trap_25, 'w')
I_trap25, h_trap25 =trapezoidal(f, 1, 3, 25, name_trap_25)

name_simp_5='Simpson(2) N=5.txt'
file=open(name_simp_5, 'w')
I_simp5, h_simp5 =simpson(f, 1, 3, 5, name_simp_5)

name_simp_10='Simpson(2) N=10.txt'
file=open(name_simp_10, 'w')
I_simp10, h_simp10 =simpson(f, 1, 3, 10, name_simp_10)

name_simp_25='Simpson(2) N=25.txt'
file=open(name_simp_25, 'w')
I_simp25, h_simp25 =simpson(f, 1, 3, 25, name_simp_25)

#actual value
I=1.306852819
#printing in tabular format
print('{0:20}'.format('Actual Value'),'{0:10}'.format('N'),'{0:20}'.format('Midpoint'), '{0:20}'.format('Trapezoid'), '{0:20}'.format('Simpson'),'\n'
      '{0:20}'.format(''),'{0:10}'.format(f'{5}'),'{0:20}'.format(f'{I_mid5}'), '{0:20}'.format(f'{I_trap5}'), '{0:20}'.format(f'{I_simp5}'),'\n'
      '{0:20}'.format(f'{I}'),'{0:10}'.format(f'{10}'),'{0:20}'.format(f'{I_mid10}'), '{0:20}'.format(f'{I_trap10}'), '{0:20}'.format(f'{I_simp10}'),'\n'
      '{0:20}'.format(''),'{0:10}'.format(f'{25}'),'{0:20}'.format(f'{I_mid25}'), '{0:20}'.format(f'{I_trap25}'), '{0:20}'.format(f'{I_simp25}'),'\n')
