import requests

BASE="http://127.0.0.1:5000/"


# response = requests.get(BASE + "startup")
value = "S"
response = requests.get(BASE + "search", json={"search": value})

print(response.json())
