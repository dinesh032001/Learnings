"""
#1
L=int(input('Enter the length:'))
B=int(input('Enter the breadth:'))
print('Length=',L)
print('Breadth=',B)
if(L==B):
    print('It is a square')
else:
    print('It is a Rectangle')

#2
a=4
b=7
if(a>b):
    print(a)
    print('a is Greater')
else:
    print(b)
    print('b is Greater')


#3
Qty=int(input('Enter the Quantity:'))
if Qty*100>1000:
    print("Cost is",((Qty*100)-(.2*Qty*100)))
else:
    print("Cost is",Qty*100)

#4
   
Salary=int(input('Enter the Salary:'))
Year=int(input('Enter the Year of Service:'))
if Year>5:
    print("Bonus is",5*Salary)
else:
    print("No Bonus")

#5
Marks=int(input('Enter Your Marks:'))
if Marks<25:
    print('F')
elif Marks>=25 and Marks<45:
    print('E')
elif Marks>=45 and Marks<50:
    print('D')
elif Marks>=50 and Marks<60:
    print('C')
elif Marks>=60 and Marks<80:
    print('B')
else:
    print('A')

#6
Sai=int(input('Enter Your Age:'))
Raju=int(input('Enter Your Age:'))
Hari=int(input('Enter Your Age:'))
if Sai>Raju and Sai>Hari:
    print('Oldest Age is',Sai)
elif Raju>Sai and Raju>Hari:
    print('Oldest Age is',Raju)
elif Hari>Sai and Hari>Raju:
    print('Oldest Age is',Hari)
else:
    print("All are equal")



#7&8
a=int(input('Total no.of classes held:'))
b=int(input('Total no.of classes attended:'))

Y=True
N=False
medical_cause=True
medical_cause1=False
percent=(b/float(a))*100
print("Attendence is",percent)
if percent>=75:
    print("You are allowed")
else:
    print("Sorry, you are not allowed")
if medical_cause==N:
    print("You are allowed to write exam")
else:
    if percent>=75:
     print("You are allowed",medical_cause)
    else:
     print("Sorry,not allowed")
   """  



