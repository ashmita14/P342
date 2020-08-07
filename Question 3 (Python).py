#Question 3

sum=0.0
n=int(input("Enter value of n:\n"))
for i in range(n):
    m=i+1.0
    diff=sum
    sum=sum+1.0/m
    diff=sum-diff
    if diff<=0.001 :
        print(f'Sum does not change by more than 0.001, so operation terminated after adding upto 1/{i}')
        break
    #
print(f'Sum = {sum}')