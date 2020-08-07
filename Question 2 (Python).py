#Question 2

fac=1
n=int(input("Enter an integer n :\n"))
if n>=0 :
    for i in range (n) :
        m=i+1
        fac=fac*m
    print(f'Factorial = {fac}')
else:
    print(f'{n} is a negative integer')

