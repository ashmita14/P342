#Question 1a

#Given number of points in  line
N=6
#number of ways a pair can be chosen
totp=N*N
totdis=0
for i in range(N): #chooses first point
    dist=0
    for j in range(N): #chooses second point
        dist=abs(i-j)
        totdis+=dist
        #
    #
avgdis=totdis/totp
print(f'Total number of points in a line = {N}')
print(f'Total number of pairs possible = {totp}')
print(f'Total Distance = {totdis}')
print(f'Average Distance = {avgdis}')