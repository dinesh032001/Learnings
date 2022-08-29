"""
#1 Factorial of a number
i=int(input("Enter the Number:",))
f1=1
while(i>0):
    f1=f1*i
    i=i-1
print('Factorial of a Number:',f1)

#2 Adding string in list
L1=[1,2,3]
L1.append('Four')
print(L1)

#3 Print 0 to 100 skip count of 5
a=int(input("Enter the Number:"))
b=0
while(b<a):
    b=b+1
    if b%5==0:
      continue
    else:
        print("The Skip Count of 5 is:",b)
      
#4 Print even numbers upto 100
c=int(input("Enter the Number:"))
d=0
while(d<=c):
    d=d+1
    if d%2==0:
        print("The Even Numbers is:",d)
    else:
       continue
    
#5 Armstrong
e=int(input("Enter the Number:"))
sum=0
org=e
while(e>0):								
    sum=sum+(e%10)*(e%10)*(e%10)
    e=e//10
if(org==sum):
    print('Its Armstrong')
else:
    print('Its Not Armstrong')

#6 Palindrome
f=(input("Enter the Number:"))
g=f[::-1]
if(f==g):
   print("It is Palindrome")
else:
    print("It is not Palindrome")

#7 Print Even Numbers from 51 to 100
c=int(input("Enter the Number:"))
d=51
while(d<=c):
    d=d+1
    if d%2==0:
        print("The Even Numbers is:",d)
    else:
       continue

#8 Print odd numbers from 1 to 25
i=0
while(i<=25):
    i=i+1
    if i%2==0:
       continue
    else:
        print("The Odd Numbers is:",i)

#9 Divisible by 7 upto 200
c=int(input("Enter the Number:"))                         
d=0
while(d<=c):
    d=d+1
    if d%7==0:
        print(d)
    else:
       continue

#10 Fibonacci series
n=int(input("Enter the terms:"))
n1=[0,1]
if n>2:
    for i in range(2,n):
        nextele=n1[i-1]+n1[i-2]
        n1.append(nextele)
print(n1)        
 
#11 Python patterns

for n in range(0,5):
    for i in range(1,n+1):
        print('*',end="")
    print("/n")    
 """       


#Functions

#1 Variable length of arguments
def num(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2
num=(10,20)
  

