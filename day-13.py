class Employee:
    pass
    def __init__(self):
        self.no=12
        self.name="Deepjyoti"
        print(self.no)
        print(self.name)


obj = Employee()  #constructor call
#print(obj)
obj1= Employee()   # constructor call

#print(obj1)


class Employee:
    pass
    no_of_emps=0; #class variable
    def __init__(self,first,last,salary):
        #instance variables
        self.first=first
        self.last=last
        self.salary=salary
        self.email=first.lower()+"."+last.lower()+"@abc.com"
        Employee.no_of_emps +=1
        
    def fullname(self): # instance method
        return self.first+" "+self.last
        
obj11 = Employee("Deepjyoti","Das","12345")
obj12 = Employee("Pohor","Debbarma","76464")
#print(obj11.first)
print(obj11.email)

print(obj11.fullname())

print(Employee.fullname(obj11))
print(Employee.no_of_emps)