#Question 1b

cross="\u2716"
#given number of points in a row = 6, we consider a 6 cross 6 grid
N=6
#total number of points in grid
NN=N*N
#Number of pairs possible
totp=NN*NN
totdis=0

for i in range(N):
    for j in range(N): #first two loops choose first point from grid
        dist=0;
        for k in range(N):
            for l in range(N): #second two loops choose the second point and traverse the entire grid
                dist=abs(i-k)+abs(j-l)
                totdis+=dist
                #
            #
        #
    #
avgdis=totdis/totp
print(f'Number of elements in {N} {cross} {N} matrix = {NN}')
print(f'Total number of pairs possible = {totp}')
print(f'Total Distance = {totdis}')
print(f'Average Distance = {avgdis}')
