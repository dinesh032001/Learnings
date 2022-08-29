"""
#Write
f=open("MSD.txt",'w')
f.write("This is Python ")
f.write("\nHello World")
f.close()



#Read
f=open("MSD.txt")
r=f.read()
print("Reading contents are:",r)



#To read few bytes
f=open("MSD.txt")
r=f.read(8)
print("Reading contents are:",r)



f=open("MSD.txt",'w')
f.write("Hello World")
f.write("\nThis is Python ")
f.close()



f=open("MSD.txt",'a')
f.write("\nThis is Object Oriented Programming Language")
f.close()



E=("Hello World")
f=open("Test.txt",'w+')
f.write(E)
d=f.read()
print("contents are:",d)



E=("Hello World")
f=open("Test.txt",'w+')
f.write(E)
f=open("Test.txt")
d=f.read()
print("contents are:",d)



E="Hello World! \nWelcome to ISM"
f=open("Test.txt",'w+')
f.write(E)
f.close()
f1=open("Test.txt")
d=f1.read()
print("contents are:",d)



f=open("Test.txt")
for x in f:
    print(x)
f.close()


#readlines    #reads line by line and returns a list where every line is a element
#can't read escape sequence characters
d1=open("Test.txt")
s=d1.readlines()
print(s)



f=open("ISM.txt",'w')
print(f.tell())
f.write("Welcome to ISM UNIV")
print(f.tell())
f.close()



f=open("ISM.txt")
print(f.read(8))
f.seek(0,1)
print(f.read())
f.close()

f= open("xyz.txt")
for line in f:
    print(line)
f.close()


newFile= open("file_name.txt ","wb")
newFile.write(b'Welcome to ISM')
newFile.close()
newFile=open("file_name.txt ","rb")
print(newFile.read())
newFile.close()



import os.path
r="C:\import file"
n=os.path.join(r, "test1.txt")
o=open(n,'w')
o.write('Hi Guys,Welcome to ISM')
o.close()

        
"""
