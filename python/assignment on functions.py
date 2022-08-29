"""
#1 Variable length arguments
def info(arg1,*arg2):
    print("Output is:")
    print(arg1)
    for i in arg2:
        print(i)
    print(len(arg2)+1)
    return
info(18)
info(20,30,40)

#2 Return Multiple Values from a function

def fun():
    str="ISM UNIV"
    x=10
    y=20
    return[str,x,y]
list=fun()
print(list)

#3 To Print the reverse of a number
def reverse(num):
    t=0
    while(num>0):
        t=t*10+(num%10)
        num=num//10
    return t
    
r=reverse(5432)
print(r)


#4 Function with default argument
def fun1(name="Dinesh",age=22,place="BLR"):
        print("Name is:",name)
        print("Age is:",age)
        print("Place is:",place)
        return 
fun1(age=20)
fun1("Name1")

#5 Innern function to calculate the addition in the following way
def fun(a,b):
    def sum(a,b):
        return a+b
        
    return sum(a,b)+5    
res=fun(5,11)
print(res)
"""
#6 Function and call it through the new name
def fun(a,b):
    print(a,b)
run=fun
run(2,4)
