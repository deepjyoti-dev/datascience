
#city = "agartala"

api = "http://api.openweathermap.org/data/2.5/weather?q=agartala&appid=b560929d461f4c1f06993bb374d15202"

import requests

response = requests.get(api)

jsondata = response.json()

jsondata['main']['temp']