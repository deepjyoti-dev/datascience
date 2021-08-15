"""
Code Challenge
  Name: 
    Get Air Pollution by using city name
  Filename: 
    cityairquality.py
  Problem Statement:
    Take the name of the city from the user through cmd and show the 
    air quality parameteres using openmapweather api. This API requires 
    lat long of place to get air quality.
    
    You need to search for an API to convert your city name to Lat-Long.
  Hint:
    https://openweathermap.org/api/air-pollution
    you need to search for a api for convert your city to Lat-Lon
    
"""




#Enter city name
city_name=input('Enter the name of the city: ')

import requests
geo_city="http://api.openweathermap.org/geo/1.0/direct?q="+city_name+"&limit=1&appid=f6a83834813667ac6507638cb6ae37d2"
city_resp=requests.get(geo_city)
print (city_resp.json()[0])


#Get Lat-Lon from the JSON using REST API
latitude_city=str(city_resp.json()[0]['lat'])
longitude_city=str(city_resp.json()[0]['lon'])

#call the api for air quality
air_city="http://api.openweathermap.org/data/2.5/air_pollution?lat="+latitude_city+"&lon="+longitude_city+"&appid=f6a83834813667ac6507638cb6ae37d2"
resp=requests.get(air_city)

print (resp.json())



