import re as r

l_city = open('largest_cities_germany.txt','r')

l_data = l_city.readlines()

city_list = []
regex = r.compile('\s[\w\s]*\s+')

for city_data in l_data:
    c_name = regex.search(city_data)[0]
    city_list.append(c_name.strip())
    
city_codes = {}

c_file=open('postal_codes_germany.txt','r')
c_data=c_file.read()

for city in city_list:

    reg_exp = '\s'+city+'\s[\d]+\s'
    c_match =  (r.findall(reg_exp,c_data)[0:3])
    c_str = " ".join(c_match) 
    city_codes[city] = r.findall(r'[0-9]+', c_str)
    
    
print (city_codes)












