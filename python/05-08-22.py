"""
#Operator Overloading:
#('+' Operator)

class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __add__(self, v):
        return self.b+v.b,self.c+v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1+s2)

s3=User("hi",'6')     
s4=User(" how are you?",'5')     
print(s3+s4)

s5=User("hi",10)   
s6=User('4',5)   
print(s5+s6)


#('-' Operator)
class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __sub__(self, v):
        return self.b-v.b,self.c-v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1-s2)

#s3=User("hi",'6')     
#s4=User(" how are you?",'5')     
#print(s3-s4)

s5=User(4,10)   
s6=User(4,5)   
print(s5-s6)


#('/' Operator)
class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __truediv__(self, v):
        return self.b/v.b,self.c/v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1/s2)

#s3=User("hi",'6')     
#s4=User(" how are you?",'5')     
#print(s3-s4)

s5=User(4,10)   
s6=User(4,5)   
print(s5/s6)


#('//' Operator)
class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __floordiv__(self, v):
        return self.b//v.b,self.c//v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1//s2)

#s3=User("hi",'6')     
#s4=User(" how are you?",'5')     
#print(s3//s4)

s5=User(4,10)   
s6=User(4,5)   
print(s5//s6)



#('**' Operator)
class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __pow__(self, v):
        return self.b**v.b,self.c**v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1**s2)

#s3=User("hi",'6')     
#s4=User(" how are you?",'5')     
#print(s3**s4)

s5=User(4,10)   
s6=User(4,5)   
print(s5**s6)


#('*' Operator)
class User():
    def __init__(self, b,c):
        self.b=b
        self.c=c
    def __mul__(self, v):
        return self.b*v.b,self.c*v.c
    def f1(s,t):
        print("Inside Method f1")
s1=User(2,4)
s2=User(5,10)
print(s1*s2)

#s3=User("hi",6)     
#s4=User(" how are you?",5)     
#print(s3*s4)

s5=User(4,10)   
s6=User(4,5)   
print(s5*s6)



#Single Level:
class A():    #parent class/Base class
    def m1(self):
        print('inside method m1')        
#class childclass(Baseclass)        
class B(A):    #derived class from class A
    def m2(s):
        print('inside method m2')
ob1=A()
ob2=B()
ob1.m1()
ob2.m2()
ob2.m1()
print(dir(A))
print(dir(B))


class A():
    a=10
class B(A):    
    b=20
ob1=A()
ob2=B()
print(ob1.a)
print(ob2.b)
print(ob2.a)
ob2.a=30
print(ob2.a)
print(ob1.a)


class A():   
    def m1(self):
        print('inside method m1-class A')          
class B(A):  
    def m1(s):
        print('inside method m1-class B')
ob1=A()
ob2=B()
ob1.m1()
ob2.m1()    #Method over-riding


class A():
    __a1=10
class B(A):    
    b1=20
ob1=A()
ob2=B()
print(ob1._A__a1)
print(ob2._A__a1)
print(dir(A))
print(dir(B))
#print(ob2._B__a1)    #Error: private data: it is available as _A__a1


#Multilevel:
class A():
    a=10
class B(A):
    b=20
class C(B):
    c=30
ob1=A()
ob2=B()
ob3=C()
print(ob1.a)
print(ob2.a)
print(ob2.b)
print(ob3.c)
print(ob3.b)
ob3.c=40
print(ob3.c)



#Multiple:
class A():
    a=1
class B():
    b=2
class C():
    c=3
class D(A,B,C):
    d=4
ob1=A()
ob2=B()
ob3=C()
ob4=D()
print(ob1.a)
print(ob2.b)
print(ob3.c)
print(ob4.a)
print(ob4.b)
print(ob4.c)
print(ob4.d)


#Hybrid:
class A():
    a=1
class B():
    b=2
class C(A):
    c=3
class D(A,B):
    d=4
class E(C):
    e=5
ob1=A()
ob2=B()
ob3=C()
ob4=D()
ob5=E()
print(ob1.a)
print(ob2.b)
print(ob3.c)
print(ob3.a)
print(ob4.d)
print(ob4.a)
print(ob4.b)
print(ob5.e)
print(ob5.c)
print(ob5.a)

"""
#Assignment 
class A:
    def add(self,x,y):
        print(x+y)
class B(A):
    def add(self,x,y,z):
        print(x+y+z)
        
p=B()
p.add(1,4,2)

q=A()
q.add(1,4)









