"""
class Calc1:
    def Summation(self,a,b):
        return a+b;
class Calc2:
    def Multiiplication(self,a,b):
        return a*b;
class Calc3:
    def Subtraction(self,a,b):
        return a-b;
class Derived(Calc1,Calc2):
    def Divide(self,a,b):
        return a/b;
d=Derived()
print(isinstance(d,Calc1))
print(isinstance(d,Calc3))



class A():
    print("This is A")
class B():
    print('This is B')
x=A()
x1=B()
print(isinstance(x,A))
print(isinstance(x,B))
print(isinstance(x1,B))
print(isinstance(x1,A))


class A():
    print("This is A")
class B(A):
    print('This is B')
x=A()
x1=B()
print(isinstance(x,A))
print(isinstance(x,B))
print(isinstance(x1,B))
print(isinstance(x1,A))


try:
    print('Hey')
    print(c)
    print('Hi')
except:
    print('Error in try block')
print("End")    


try:
    print('Hey')
    print('Hi')
except:
    print('Error in try block')
    print("End")    


try:
    print('Hey')
    print('10'+100)
    print('Hi')
except:
    print('Error in try block')
print("End")


try:
    print('Hey')
    print(a)
    print('Hi')
except NameError:
    print("a is not defined")
except TypeError:
    print('Error in try block')
print("End")    


x=int(input('Enter a Number-'))
y=int(input('Enter Another Number-'))
try:
    print("Quotient is:",x/y)
except:
    print("You are trying to divide a number by zero!!!")
    y=int(input('Re-Enter the Second Number other than 0-'))
    print(x/y)
print("End")        
         

x=int(input('Enter a Number-'))
y=int(input('Enter Another Number-'))
try:
    print("Quotient is:",x/y)
    print(c)
except ZeroDivisionError:
    print("You are trying to divide a number by zero!!!")
    y=int(input('Re-Enter the Second Number other than 0-'))
    print(x/y)
except:
    print("You haven't defined c variable!!!!")
    c=3
    print("C value is:",c)
print("End")




try:
    print('Hey')
    print(c)
    print('Hi')
except TypeError:
    print('Error in try block')
except:
    print("You haven't defined c variable!!!!")    
print("End")    



def a():
    try:
        f(x,4)
    finally:
        print('after f')
    print('after f?')
a()    
"""


