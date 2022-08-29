#Class & Objects
"""
print(dir())
print("Hello")
class Abc():
    print("This is class")
    _a=4
    def m1(x):
        print("This is method")
print('contents of class A:\n', dir(Abc))
print(dir())
print('creating object')
ob1=Abc()     
print("accessing class variable : 'a' ")
print(ob1._a)
print('calling method m1')
ob1.m1()
print(dir())
print('contents of ob1:\n', dir(ob1))

        
class Abc():
    a=10
    def m1(self):     
        print(self)
        print(type(self))
        print(dir(self))
        print("inside method m1")
ob1=Abc()
print(ob1)
print(type(ob1))
ob1.m1()



class Abc():
    a=10
    def m1(self):     
        print(self)
        print("inside method m1")
ob1=Abc()
print('value of ob1 is:', ob1)
print(type(ob1))
ob1.m1()
ob2=Abc()
print('value of ob2 is:', ob2)
print(type(ob2))
ob2.m1()


class Abc():
    a=10
    print("HI")
    def m1(self,a):
        print(a)
        print("inside method m1")
ob1=Abc()
ob1.m1(5)


class Abc():
    a=10 #class variable
    print("ISM")
    def m1(self,x):      #'x' is local
        print("inside method m1")
        print(x)
        print('value of a is:', self.a)
ob1=Abc()
ob1.m1(67.90)
ob1.a=30
ob2=Abc()
ob2.m1("hi")



class Fun():
    c="hi"
    #z=20
    def f1(f,v):
        f.z=v
        print('inside method f1')
        print('value of v is:', v)
        print('value of c is:', f.c)
    def f2(x):
        print('value of c is:', x.c)
        print('value of v is:', x.z)
s=Fun()
s.f1(20)
s.f2()
print(s.z)


class Fun():
    c="hi"
    def f1(f,v):
        f.z=v
        print('inside method f1')
        print('value of v is:', v)
        print('value of c is:', f.c)
    def f2(x):
        print('value of c is:', x.c)
        print('value of v is:', x.z)       #'z' is not defined
s=Fun()
#s.f1(20)
s.f2()



#Constructor
class puppy(object):
    def __init__(s,n,c):
        s.n=c
        s.c=n
    def bark(s):
        print("I am",s.n,s.c)
puppy1=puppy("Max","Brown")
puppy1.bark()
puppy2=puppy("Mark","white")
puppy2.bark()


class Fun():
    print("inside the class")
    c="hi"
    def __init__(self):     #constructor
        print("inside the constructor")
    def f1(f,v):
        print('inside method f1')
        print('value of v is:', v)
        print('value of c is:', f.c)
    def f2(x):
        print('value of c is:', x.c)
        print('value of v is:', x.z)  #Error: z is not defined 
s=Fun()
s.f1(2)
s.f2()


class Fun():
    print("inside the class")
    c="hi"
    def __init__(self,g):   
        print("inside the constructor")
        print('value of g is:', g)
    def f1(f,v):
        print('inside method f1')
        print('value of v is:', v)
    def f2(x):
         print('inside method f2')
s=Fun(67)     #__init__ is called
s.f1(56)
s.f2()



class Fun():
    print("inside the class")
    c="hi"
    def __init__(self,g):
        self.g=g
        print("inside the constructor")
    def f1(f,v):
        print('inside method f1')
        print('value of g is:', f.g)
        print('value of v is:', v)
    def f2(x):
         print('inside method f2')
         print('value of g is:', x.g)
s=Fun(67)    
s.f1(56)
s.f2()


class Op():
    def __init__(w,x,y):
        w.a=x
        w.b=y        
    def add(se):
        print('inside add method')
        return se.a+se.b
    def sub(lf):
        print('inside sub method')
        return lf.a-lf.b
x=int(input('Enter a number-'))
y=int(input('Enter another number-'))
c=Op(x,y)
z=c.add()
print('sum is:',z)
q=c.sub()
print('difference is:',q)

"""















