#

import math
import sys
sys.path.append('C:/ASHMITA/NISER Study/5th Semester/P342 - Computational Lab/APanda_Lib')
#importing all files at once, now we just need to write function name to access it
from APanda_Lib import *

f=lambda x: math.exp(-x*x)

#MIDPOINT
name_mid='Midpoint by Error.txt'
file=open(name_mid, 'w')
I_mid, h_mid=midpoint_error(f, 0, 1, 0.001, name_mid)

#TRAPEZOIDAL
name_trap='Trapezoidal by Error.txt'
file=open(name_trap, 'w')
I_trap, h_trap=trapezoidal_error(f, 0, 1, 0.001, name_trap)

#SIMPSON
name_simp='Simpson by Error.txt'
file=open(name_simp, 'w')
I_simp, h_simp=simpson_error(f, 0, 1, 0.001, name_simp)

#actual integration value
I=0.7468241

print('{0:20}'.format('Actual Value'), '{0:10}'.format('Error'), '{0:20}'.format('Midpoint'), '{0:20}'.format('Trapezoid'),
      '{0:20}'.format('Simpson'), '\n'
                                  '{0:20}'.format(f'{I}'), '{0:10}'.format(f'{0.001}'), '{0:20}'.format(f'{I_mid}'),
      '{0:20}'.format(f'{I_trap}'), '{0:20}'.format(f'{I_simp}'), '\n')