"""
class c:
    def __init__(s,a):
        s.a=a
    def display(s):
        print(s.a)
ob=c()
ob.display()

#Data Encapsulation:
class Op():
    x=10
    __y= "hi"
    _z=[1,2,3]
v=Op()
print(v.x)
print(v._z)
#print(v.__y)
print(v._Op__y)
v._Op__y=20
print(v._Op__y)


class Op():
   def __m1(s):
       print('inside m1')
v=Op()
v._Op__m1()


#Function over-riding:
def f1():
    print('inside function f1')
def f1():
    print('inside function f1- second definition')
f1()


#Function over-loading:
def f1(x):
    print(x)
f1(10,345,80)


def f1(*x):
    print(x)
f1(10,345,80)


def f1(*x):
    print(x)
def f1(x,y,z):
    print(x)
    print(y)
    print(z)
#f1(10)     #error: Over-loading is not supported
f1(70,20,30)
"""

class fruit():
    def __init__(s):
        s.price=100
        s.__bags=10
    def get(s):
        return s.__bags
obj=fruit()
print(obj._fruit__bags)





