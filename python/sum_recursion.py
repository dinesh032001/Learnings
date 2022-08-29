def sum(n):
    if n==1:
        return 1
    elif n<0:
        return -1
    else:
        return n+sum(n-1)

print("sum of digits for 5:",sum(5))