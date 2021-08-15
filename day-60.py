
currencyapi = "https://free.currencyconverterapi.com/api/v6/convert?q=INR_USD&compact=ultra&apiKey=7a276e3336d5cd40d295"

import requests

response = requests.get(currencyapi)

jsondata = response.json()



#POST API Call

api = "http://httpbin.org/post"

import requests

import json

data = {
 'firstname': "James",
 'skills': "Python"
 
 }


headers = {
    "Content-Type": "application/json",
    "Content-Length": len(data),
    "data": json.dumps(data)
    
    }

response = requests.post(api,data,headers )

response.json()['form']










sts.post