def factorial(n):
    t=n
    fact=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(n):
            fact*=t
            t=t-1
        return fact

print(factorial(5))