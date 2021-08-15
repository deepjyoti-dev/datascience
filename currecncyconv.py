"""
    Develop a Currency Converter which Converts an unit USD to INR

    You need to fetch the current conversion prices from the JSON response
    using REST API call.
    
    
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8b3cff2e1d2dfd79de05"

res = requests.get(url)

data = res.json()
print(data['USD_INR'])


