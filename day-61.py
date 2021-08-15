

import requests
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8b3cff2e1d2dfd79de05"

obj = requests.get(url)

data = obj.json()
print(data['USD_INR'])


