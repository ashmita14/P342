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