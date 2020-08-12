#Question 2

import array as arr

A=arr.array('i',[3,8,7])
B=arr.array('i',[5,2,9])

S=arr.array('i',[0,0,0])
D=arr.array('i',[0,0,0])
for i in range(0,3):
    S[i]=A[i]+B[i]
    D[i]=A[i]*B[i]

print("Vector A = [", end=" ")
for i in range(0,3):
    print(A[i], end=" ")
print("]")
print( )

print("Vector B = [", end=" ")
for i in range(0,3):
    print(B[i], end=" ")
print("]")
print( )

print("Sum of A and B = [", end=" ")
for i in range(0,3):
    print(S[i], end=" ")
print("]")
print( )

print("Dot product of A and B = [", end=" ")
for i in range(0,3):
    print(D[i], end=" ")
print("]")
print( )



######OUTPUT####### (directly copy pasted from the run window)
#Vector A = [ 3 8 7 ]
#
#Vector B = [ 5 2 9 ]
#
#Sum of A and B = [ 8 10 16 ]
#
#Dot product of A and B = [ 15 16 63 ]
