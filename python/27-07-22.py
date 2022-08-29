"""
def outerfun(a,b):
    def innerfun(c,d):
        return c+d
    return innerfun(a,b)
    return a

result=outerfun(5,10)
print(result)

i=6

def f(arg=i):
    print(arg)

i=5
f()

def f(i):
    print(i,type(i))
a={'p':10,'q':20,'r':30}
f(a)

def fun(name):
    """docstring"""
    print("Hello" +name)
fun(" ISM")
"""
fun(" ISM")
