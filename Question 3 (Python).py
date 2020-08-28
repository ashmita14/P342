#Question 3
#Matrix A :
#  1 -3  7
# -1 4  -7
# -1 3  -6

n=3  #dimension of square matrix, ie n cross n matrix
cross="\u2716" #cross symbol

#function for partial pivoting
def partial(x):
    for i in range(0,n-1): #loops from 0 to n-2,i.e., upto second last row
        if x[i][i]==0:
            val=0 #will use val to swap rows
            for j in range(i+1,n): #loops from i+1 to n-1
                if abs(x[j][i])>x[i][i]:
                    for k in range(2*n): #2n because aug matrix is n cross 2n, loop for swapping the rows, k gives us column number
                        val=x[i][k]  #i ==> row with 0 in pivot position
                        x[i][k]=x[j][k] #j ==> row with which ith row is being swapped
                        x[j][k]=val
                    #
                #
            #
        #
    #we now consider the last row, for some exceptional case where only the last pivot is zero
    i=n-1 #last row
    if x[i][i]==0:
        j=n-2
        while j>=0:
            # we can exchange with row j only if a_{j}{i} is not zero,
            # if it is zero, then the exchange will put a zero in pivot position of row j
            if abs(x[j][i])>x[i][i] and x[i][j]!=0:
                for k in range(0,2*n): #loop for column
                    val = x[i][k]  # i ==> row with 0 in pivot position
                    x[i][k] = x[j][k]  # j ==> row with which ith row is being swapped
                    x[j][k] = val
                    #
                #
            j=j-1
            #
        #
    #

#function for gauss jordan
def gauss_jordan(x):
    partial(x); #partial pivoting
    for i in range(n): #loops from 0 t n-1
        pivot=x[i][i]
        if pivot!=0:
            for k in range(i,2*n): #loops from ith position to nth position, necessary for columns as augmented matrix has n+1 columns
                x[i][k]=float(x[i][k])/float(pivot) #diving elements of that row with the pivot element
                #
            for r in range(n): #to make all elements in column of pivot element (ith column) zero
                if r==i or x[r][i]==0: continue
                else:
                    subtr=x[r][i] #value of element in rth row below pivot which we need to convert to zero
                    for k in range(i,2*n):
                        x[r][k]=x[r][k]-subtr*x[i][k]
                        #
                    #
                #
            #
        else: print(f'Pivot value at position {i}{i} is zero')
    #

#Multiplication function
def multiply(x,y,xy):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                xy[i][j]=xy[i][j]+x[i][k]*y[k][j]
                #
            #
        #
    print("Matrix obtained after multiplication : ")
    print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in xy]))
    #

f=open('A of Ques 3.txt', 'r') #'r' ==> read only
A=[[int(num) for num in line.split(' ')] for line in f] #Matrix A
print("The Matrix A : ")
print('\n'.join([''.join(['{0:6}'.format(item) for item in row]) for row in A]))
#converting it into an augmented matrix, for finding inverse
#augmented matrix will have A and an n cross n identity matrix,
# so it will become a n(row) cross 2n(column) matrix
Aug=[[0 for j in range(2*n)] for i in range(n)]
for i in range(n): #rows
    for j in range(2*n): #columns
        if j<3: Aug[i][j]=A[i][j]
        else:
            m=j-3
            if m==i: Aug[i][j]=1
            #
        #
    #
print("Augmented Matrix : ")
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in Aug]))
#calling function for partial pivoting of augmented matrix
partial(Aug);
print("After partial pivoting of Augmented Matrix : ")
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in Aug]))
#calling function for gauss-jordan method
gauss_jordan(Aug);
print("Augmented matrix after Gauss-Jordan Elimination : ")
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in Aug]))
inv_A=[[0 for j in range(n)]for i in range(n)]
#extracting inverse matrix from Augmented Matrix
for i in range(n):
    for j in range(2*n): #fornavigating all the columns of augmented matrix
        if j>2:
            m=j-3
            inv_A[i][m]=Aug[i][j]
            #
        #
    #
print("Inverse Obtained by Gauss-Jordan Process : ")
print('\n'.join([''.join(['{0:6}'.format(item) for item in row])for row in inv_A]))
#we call multiplication function to check if inverse obtained by Gauss-Jordan method is correct or not
AA_1=[[0 for j in range(n)]for i in range(n)] #matrix to hold the multiplication value of A and inv_A
multiply(A,inv_A,AA_1);
#defining n cross n identity matrix
I=[[0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j: I[i][j]=1
        #
    #
#checking if inverse obtained is correct
if AA_1==I: print(f'The multiplication matrix obtained is equal to the {n}{cross}{n} Identity matrix, thus the inverse computed by Gauss-Jordan method is correct.')
else: print("The inverse coputed by Gauss-Jordan method is incorrect.")

    
    
    
 
######### OUTPUT ############ (DIRECTLY COPY PASTED FROM RUN WINDOW)
#The Matrix A : 
#     1    -3     7
#    -1     4    -7
#    -1     3    -6
#Augmented Matrix : 
#     1    -3     7     1     0     0
#    -1     4    -7     0     1     0
#    -1     3    -6     0     0     1
#After partial pivoting of Augmented Matrix : 
#     1    -3     7     1     0     0
#    -1     4    -7     0     1     0
#    -1     3    -6     0     0     1
#Augmented matrix after Gauss-Jordan Elimination : 
#   1.0   0.0   0.0  -3.0   3.0  -7.0
#   0.0   1.0   0.0   1.0   1.0   0.0
#   0.0   0.0   1.0   1.0   0.0   1.0
#Inverse Obtained by Gauss-Jordan Process : 
#  -3.0   3.0  -7.0
#   1.0   1.0   0.0
#   1.0   0.0   1.0
#Matrix obtained after multiplication : 
#   1.0   0.0   0.0
#   0.0   1.0   0.0
#   0.0   0.0   1.0
#The multiplication matrix obtained is equal to the 3✖3 Identity matrix, thus the inverse computed by Gauss-Jordan method is correct.
#
#Process finished with exit code 0

