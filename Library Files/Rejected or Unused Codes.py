#codes rejected due to unnecessary complexity or other reasons

# FINDING ABSOLUTE ERROR FROM VALUES IN FILE
def absolute_error(x, y): #parameter = names of - original datafile, datafile to store abslute error values
    X=read_matrix(x)
    n=len(X) #no. of rows
    m=len(X[0]) #no. of columns
    #x_{n+1}-x_n is absolute error
    for i in range(n-1):
        if m>0: #leaving first column, as it may represent serial number, or some counter;
            for j in range(1,m):
                X[i][j]=abs(X[i+1][j]-X[i][j])
                #
        else: X[i][j]=abs(X[i+1][j]-X[i][j])
    #appending values to file
    for i in range(n-1):
        L=f'{X[i][0]}'
        for j in range(1,m):
            L=L+f' {X[i][j]}'
            #
        L=L+'\n'
        append_file(y, L)
        #
    #

# Bisection
def bisection(f, a, b, tot_itr, max_itr, x): #parameters = function, guesses a and b, current iteration count, total nuber of allowed iterations and file name
    err=pow(10,-6)
    mid=(a+b)/2
    #opening file, appending values and closing file
    append_file(x, f'{max_itr - tot_itr + 1} {mid}\n' )
    if round(f(mid), 6)!=0: #if f(mid)!=0 (rounded upto 6 deciml places), then mid isn't at root position
        if f(a) * f(mid) < 0: b = mid  # root lies left of mid
        if f(a) * f(mid) > 0: a = mid  # root lies right of mid
    else: #mid is at root position
        a=mid
        b=mid
    if abs(b-a)<err: #root found
        return(mid, True)
    else:
        if tot_itr>0: #proceeds if allowed number of iterations is not crossed
            return(bisection(f, a, b, tot_itr - 1, max_itr, x))
        else:
            return(mid, False)
    #

# Regula-Falsi
def regula_falsi(f, a, b, tot_itr, max_itr, x): #parameters = function, guesses a and b, current iteration count, total nuber of allowed iterations and file name
    false_c=b-(((b-a)*f(b))/(f(b)-f(a)))
    #opening file, appending values and closing file
    append_file(x, f'{max_itr - tot_itr + 1} {false_c}\n')
    if round(f(false_c), 6)!=0: #if f(false_c)!=0 (rounded upto 6 decimal places), then false_c isn't at root position
        if tot_itr>0: #proceeds if allowed number of iterations is not crossed
            if f(a) * f(false_c) < 0: return(regula_falsi(f, a, false_c, tot_itr-1, max_itr, x))
            if f(a) * f(false_c) > 0: return(regula_falsi(f, false_c, b, tot_itr-1, max_itr, x))
            #
        else: #maximum number of allowed iterations is crossed
            return(false_c, False)
    else: #false_c is at root position
        return(false_c, True)
    #
