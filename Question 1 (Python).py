#Question 1
# x+3y+2z=2
#2x+7y+7z=-1
#2x+5y+2z=7

n=3  #dimension of square matrix, ie n cross n matrix

#function for partial pivoting
def partial(x):
    for i in range(0,n-1): #loops from 0 to n-2,i.e., upto second last row
        if x[i][i]==0:
            val=0 #will use val to swap rows
            for j in range(i+1,n): #loops from i+1 to n-1
                if abs(x[j][i])>x[i][i]:
                    for k in range(n+1): #n+1 because aug matrix is n cross n+1, loop for swapping the rows, k gives us column number
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
                for k in range(0,n+1): #loop for column
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
            for k in range(i,n+1): #loops from ith position to nth position, necessary for columns as augmented matrix has n+1 columns
                x[i][k]=float(x[i][k])/float(pivot) #diving elements of that row with the pivot element
                #
            for r in range(n): #to make all elements in column of pivot element (ith column) zero
                if r==i or x[r][i]==0: continue
                else:
                    subtr=x[r][i] #value of element in rth row below pivot which we need to convert to zero
                    for k in range(i,n+1):
                        x[r][k]=x[r][k]-subtr*x[i][k]
                        #
                    #
                #
            #
        else: print(f'Pivot value at position {i}{i} is zero')
    #

f=open('Aug. Matrix 1.txt', 'r')  #'r' ==> read only
Aug=[[int(num) for num in line.split(' ')] for line in f]  #Augmented matrix of the question
print("System of equations to solve :")
print(f' x+3y+2z = 2 \n 2x+7y+7z = -1 \n 2x+5y+2z = 7')
print("Writing it as an augmented matrix :")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in Aug]))
#driver code, calling function for partial pivoting
partial(Aug);
print("After partial pivoting : ")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in Aug]))
#driver code, calling function for gauss-jordan method
gauss_jordan(Aug);
print("After application of Gauss-Jordan method, augmented matrix becomes : ")
print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in Aug]))
print(f'Thus, we can write the result as (writing x, y and z respectively as x{1},x{2} and x{3}) : ')
for i in range(n):
    if Aug[i][i]!=0: print(f'x{i+1} = {Aug[i][n]}')
    else: print(f'x{i} has arbitrary values.')
    #

    
    
####### OUTPUT ########## (DIRECTLY COPY PASTED FROM RUN WINDOW)
#System of equations to solve :
# x+3y+2z = 2 
# 2x+7y+7z = -1 
# 2x+5y+2z = 7
#Writing it as an augmented matrix :
#     1     3     2     2
#     2     7     7    -1
#     2     5     2     7
#After partial pivoting : 
#     1     3     2     2
#     2     7     7    -1
#     2     5     2     7
#After application of Gauss-Jordan method, augmented matrix becomes : 
#   1.0   0.0   0.0   3.0
#   0.0   1.0   0.0   1.0
#   0.0   0.0   1.0  -2.0
#Thus, we can write the result as (writing x, y and z respectively as x1,x2 and x3) : 
#x1 = 3.0
#x2 = 1.0
#x3 = -2.0
#
#Process finished with exit code 0
