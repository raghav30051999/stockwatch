import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=2NWBOS1G7TXTZNV0'
r = requests.get(url)
data = r.json()

print(data)