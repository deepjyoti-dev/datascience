import re as r

#print (dir(r))


string1="name email password dob"

string2 =r.findall('[^a-e]', string1)

print(string2)

email="aaa123@yahoo.com kkkk456@gmail.com jjjjj789@hotmail.com"

sub_string=r.sub('[a-z0-9]+@','deep@',email)

print(sub_string)
string32='123abc463'
string3='abcd1234pqrs5678_0987'
string4=r.findall('[a-z]{4}', string3)
string5=r.findall('\d{3}',string3)
string7=r.findall('^\d{3}',string3)
string6=r.findall('^\d{3}',string32)
print(string4)
print(string5)
print(string6)
print(string7)

string8='123avc3459'
print(r.search('\d{3}',string8))

print(r.match('avc',string8))
print(r.search('345',string8))


str1 = 'regular expression  deep@yahoo.com 3456 Done '

r.findall('\w+@\w+\.\w+', str1 )

str1 = 'regular expression 789 deep@yahoo.com Done '

e_pattern = r.compile(r'\w+@\w+\.\w+')
e_pattern.findall(str1)