import requests

url = "https://api2.binance.com/api/v3/ticker/24hr"

response = requests.request("GET", url)
print(response.json()[0])
print(response.json()[1])