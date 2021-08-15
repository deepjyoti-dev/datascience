
string="My name is deepjyoti"
print(type(string))
len(string)
string[0]
string[-1]

#indexing,slicing

string[0:8]
string[2:11]
string[6:]
string[:15]

print(dir(str))
print(help(str.upper))

string1 = string.upper()
print(string1)

string2 = string.lower()
print(string2)


#math library

import math as m

#dir(m)

x=input("\nEnter a number\n")
if (not x):
        print("Invalid input")
x1=m.sqrt(x)
print(x1)

while(True):
    x2=input("Enter a number")
    if(len(x2) == 0):
        print("Invalid input")
        break
    if(x2.isdigit()):
        x2=int(x2)
        x3=m.sqrt(x2)
        print(x3)
    else:
        print("string")
     

while(True):
    x2=input("Enter a number")
    if(len(x2) == 0):
        print("Invalid input skip this step")
        continue
    x2=int(x2)
    x3=m.sqrt(x2)
    print(x3)
    
    
list1 = []
while(True):
    x2=input("Enter a number")
    if(len(x2) == 0):
        print("Invalid input")
        continue
    if(x2.isdigit()):
        x2=int(x2)
        list1.append(m.sqrt(x2))
        print(x3)
    else:
        list1.append(len(x2))
        print("string")
    