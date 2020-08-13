#Question 2

#importing array
import array as arr

#declaring arrays
A=arr.array('i',[3,8,7])
B=arr.array('i',[5,2,9])

S=arr.array('i',[0,0,0])
D=0
for i in range(0,3):
    S[i]=A[i]+B[i]  #A+B (Sum)
    D=D+A[i]*B[i]   #A.B (Dot Product)

print("Vector A = ", end="")
print("[",','.join(['{:2}'.format(item) for item in A]), " ]")
print( )

print("Vector B = ", end=" ")
print("[",','.join(['{:2}'.format(item) for item in B]), " ]")
print( )

print("Sum of A and B = ", end=" ")
print("[",','.join(['{:3}'.format(item) for item in S]), " ]")
print( )

print(f'Dot product of A and B = {D}')
print( )


######OUTPUT####### (directly copy pasted from the run window and converted to comment using #)
#Vector A = [  3, 8, 7  ]
#
#Vector B =  [  5, 2, 9  ]
#
#Sum of A and B =  [   8, 10, 16  ]
#
#Dot product of A and B = 94
#
#
#Process finished with exit code 0
