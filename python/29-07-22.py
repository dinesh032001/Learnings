"""
def disp(**kwargs):
    #Function
    for i in kwargs:
        print(i)
disp(emp="kelly",salary=9000)
print(disp.__doc__)

def sum(*args):
    r=0
    for i in args:
        r+=i
    return r
print(sum.__doc__)
print(sum(1,2,3))
print(sum(1,2,3,4,5))

def say(msg,times=1):
    print(msg*times)
say("Hello")
say("World",5)

def display(*arg):
    for i in arg:
        print(i)
display(name="hi",age="24")        

a=(10,22,45,30)
x=filter(lambda y:y%5==0,a)
print(x)
print(type(x))
print(list(x))

def fun(name,age=20):
    print(name,age)
fun("ISM",25)

def info(name,age):
 print("Name:",name)
 print("Age",age)
 return
info(age=50,name="Nike")
"""
