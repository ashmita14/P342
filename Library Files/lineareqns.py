#Library containing functions required to solve various systems of linear equations

#READ FILE
def read_matrix(x): #more than one column
    f=open(x,'r') #'r' ==> read only
    X=[[int(num) for num in line.split(' ')] for line in f]
    return(X)

def read_vector(x): #only one column
    f=open(x,'r') #'r' ==> read only
    X=[int(num) for num in f]
    return(X)

#PARTIAL-PIVOTING
def partial_pivot(x):
    n=len(x) #no. of rows
    m=len(x[0]) #no. of columns
    for i in range(0,n-1): #loops from 0 to n-2,i.e., up to second last row
        if x[i][i]==0:
            val=0 #will use val to swap rows
            for j in range(i+1,n): #loops from i+1 to n-1
                if abs(x[j][i])>x[i][i]:
                    for k in range(m): #loop for swapping the rows, k gives us column number
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
                for k in range(0,m): #loop for column
                    val = x[i][k]  # i ==> row with 0 in pivot position
                    x[i][k] = x[j][k]  # j ==> row with which ith row is being swapped
                    x[j][k] = val
                    #
                #
            j=j-1
            #
        #
    return(x)

#GAUSS-JORDAN METHOD
def gauss_jordan(x):
    n=len(x) #no. of rows
    m=len(x[0]) #no. of columns
    partial_pivot(x); #partial pivoting
    for i in range(n): #loops from 0 to n-1
        pivot=x[i][i]
        if pivot!=0:
            for k in range(i,m): #loops columns from ith position to end
                x[i][k]=float(x[i][k])/float(pivot) #diving elements of that row with the pivot element
                #
            for r in range(n): #to make all elements in column of pivot element (ith column) zero
                if r==i or x[r][i]==0: continue
                else:
                    subtr=x[r][i] #value of element in rth row below pivot which we need to convert to zero
                    for k in range(i,m):
                        x[r][k]=x[r][k]-subtr*x[i][k]
                        #
                    #
                #
            #
        else: print(f'Pivot value at position {i}{i} is zero')
    return(x)

#MATRIX MULTIPLICATION
def multiply(x,y):
    nx=len(x) #no. of rows in x
    mx=len(x[0]) #no. of columns in y
    ny=len(y) #no. of rows in y
    my=len(y[0]) #no. of columns in y
    xy=[[0 for j in range(my)] for i in range(nx)] #nx cross my matrix
    if mx!=ny:
        print('Matrices cannot be multiplied.')
        #
    else:
        for i in range(nx):
            for j in range(my):
                for k in range(mx):
                    xy[i][j] = xy[i][j] + x[i][k] * y[k][j]
                    #
                #
            #
        #
    return(xy)
    #

#LU DECOMPOSITION
def LU_decomposition(x): #Using Crout's method
    n=len(x) #no. of rows
    m=len(x[0]) #no. of columns
    for j in range(m): #for rows
        for i in range(n): #for columns
            if i<j: #upper-triangular ==> elements of U
                for k in range(i): #loops from 0 to i-1
                    x[i][j]=float(x[i][j]-x[i][k]*x[k][j])
                    #
                #
            if i==j: #diagonal elements of U
                for k in range(i):
                    x[j][j]=float(x[j][j]-x[j][k]*x[k][j])
                    #
                #
            if i>j: #lower diagonal ==> elements of L
                for k in range(j): #loops from 0 to j-1
                    x[i][j]=float(x[i][j]-x[i][k]*x[k][j])
                    #
                x[i][j]=x[i][j]/float(x[j][j])
            #
        #
    return(x)

#FORWARD-BACKWARD SUBSTITUTION
def forward_backward(a,b):
    # we solve (LU)X=b
    # Let UX=Y;
    # First we solve LY=b and then UX=Y
    n=len(a) #number of rows
    m=len(a[0]) #number of columns
    #we can just modify b for both X and Y because each element is used only once before modifiation

    #FORWARD SUBSTITUTION : LY=b
    for i in range(n):
        for j in range(i): # i>j (as L is lower triangular)
            b[i]=float(b[i]-a[i][j]*b[j])
            #
        #
    #BACKWARD SUBSTITUTION : UX=Y
    for i in range(3,-1,-1): #i goes in decreasing order, from 3 to 0
        for j in range(i+1,n): # i<j(as U is upper triangular)
            b[i]=b[i]-a[i][j]*b[j]
            #
        b[i]=float(b[i])/a[i][i]
        #
    return(b)

