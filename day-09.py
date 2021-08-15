
import re as r
list1 = []
fopen = open("simpsons_phone_book.txt", 'r')

for text in fopen:
    if (r.match(r'J\w+\s+(Neu)', text)):
       print (text)
       list1.append(text)
        

fopen.close()

#writing searched data to a text file
fopen1 = open("searched.txt", "w")

for data in list1:

    fopen1.write(data + "\n")

fopen1.close()
