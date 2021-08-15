

print("What should we pick up at the store?\n Enter 'DONE' to stop adding the items to list.")

list1 = []

while(True):
    get=input("Add items :  ")
    if(get.upper() == "DONE"):
        break
    else:
        list1.append(get)
        
print("The store list is :\n")
print(*list1, sep = ", ") 