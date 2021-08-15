list1 = [1,2,3,4,5,6,7]

type(list1)

dir(list)

list1.append(100)

list1[0]

list1[-1]

list1[0] = 11

list1.insert(1, 22)


list1.remove(5)


list1 = [10,5,2,5,6,5,20]

list1.count(5)

list1.remove(5)
list1.remove(5)
list1.remove(5)


list1 = [10,5,2,5,6,5,20]

while (5 in list1):
    list1.remove(5)



list1 = ['Amar','Akbar', 'Anthony']

list1[0]
list1[1]
list1[2]

list1 = ['Amar','Akbar', 'Anthony']

for name in list1:
    print (name)
    
for x in list1:
    print (x)



list1 = [1,2,3,4,5]
list2 = []

for item in list1:
    list2.append (item*item)
#[1, 4, 9, 16, 25]
    
#list comprehension    
[item*item for item in list1]


list1 = ['Amar', 'Akbar', 'Anthony']

list2 = []

for item in list1:
    list2.append(len(item))

list3 = [len(item) for item in list1]


"""
name -> Krrish
class -> 9
ssc -> 89
math -> 78

"""
student = {
 'name': 'Krrish',
 'class': 9,
 'ssc': 89,
 'math': 78
 
 }

student['ssc']

student['name'] = 'Krrish Sharma'

student['city'] = 'Amritsar'

#version 04

datastore = {}
import math
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        datastore[x] = math.sqrt(x)
    else:
        datastore[x] = (len(x))



print (datastore)











