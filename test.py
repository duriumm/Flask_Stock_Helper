from urllib import response
import requests
BASE = "http://127.0.0.1:5000/"

# Adding a stock to stocklist
response = requests.put(BASE, {"name": "Lasse name", "views": 102, "likes": 10})
print(f"Put request: {response.json()}")

# GET REQUEST
response = requests.get(BASE)
print(f"Get request: {response.json()}")