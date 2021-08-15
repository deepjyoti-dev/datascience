
class Book_details:
    
    def __init__(self, author_last, author_first, title, place, publisher, year):
        self.author_last = author_last
        self.author_first = author_first
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
  
    def write_bib_entry(self):
        return self.author_last \
               + ',' + self.author_first \
               + ',' + self.title + ',' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
  
                                                          
obj1 = Book_details( "Pilipp", "Koehn", "Neural Machine Translation", "United kingdom", "Cambridge University Press", "2020", )
obj2  = Book_details( "Douglas", "Stinson", "Cryptography", "New york","CRC press", "2019" )


print (obj1.write_bib_entry())

print(obj2.write_bib_entry())

obj2.year="2023"
print(obj2.write_bib_entry()) 
