import requests

BASE="http://127.0.0.1:5000/"

# # testing endpoint 1
# response = requests.get(BASE + "startup")

# # testing endpoint 2
# value = "hot"
# response = requests.put(BASE + "search", json={"search": value})
# print(response.json())

#testing endpoint 3
value = "S.O.S..mxl"
response = requests.put(BASE + "upload", json={"name": value})
print(response.json())
