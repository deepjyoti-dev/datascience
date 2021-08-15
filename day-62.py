
city_name=input('Enter the name of the city: ')

import requests
geo_city="http://api.openweathermap.org/geo/1.0/direct?q="+city_name+"&limit=1&appid=f6a83834813667ac6507638cb6ae37d2"
city_resp=requests.get(geo_city)
print (city_resp.json()[0])


latitude_city=str(city_resp.json()[0]['lat'])
longitude_city=str(city_resp.json()[0]['lon'])

air_quality_city="http://api.openweathermap.org/data/2.5/air_pollution?lat="+latitude_city+"&lon="+longitude_city+"&appid=f6a83834813667ac6507638cb6ae37d2"
resp=requests.get(air_quality_city)

print (resp.json())



