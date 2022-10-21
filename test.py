from urllib import response
import requests
BASE = "http://127.0.0.1:5000/"

# # Adding a stock to stocklist
# response = requests.put(BASE, {"name": "Lasse name", "views": 102, "likes": 10})
# print(f"Put request: {response.json()}")

# GET REQUEST
# response = requests.get(BASE + "stocklist")
# print(f"Get request: {response.json()}")


old_val = -5
new_val = -19
percent_diff = (float(new_val - old_val) / abs(old_val)) * 100 # abs to handle negative values
print(percent_diff)