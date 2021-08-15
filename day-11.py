

list1=[1,2,3,4,5]


def cube(y):
    return(y**3)


#print(list(map(cube,list1)))


def Check(x):
    if(x%2==0):
        return True
    else:
        return False
    
print(list(map(Check,list1)))

print(list(filter(Check,list1)))
#2nd


for data in list1:
    print(Check(data))
    

def check(y):
    return(y%2==0)

print(list(map(lambda y :y%2==0,[1,2,3,4,5])))

import functools  as fun1

def fun(a,b):
    return (a+b)
print(fun1.reduce(fun,[1,2,3,4,5]))

dict1={'name':'Deepjyoti',
       'class':'mca',
       'roll_no': 19,
       'avg':[1,2,3,4],
       'Subject':{'Math':30,'English':40,'Hindi':49}
       }
print(dict1)


dict1['name']


dict1['roll_no']=21

dict1


del dict1['class']



dict1.keys()


len(dict1)

for key in dict1.keys():
    print(key)
    
for value in dict1.values():
    print(value)
    
# dict1.clear()

print(dict1['Subject']['Math'])


