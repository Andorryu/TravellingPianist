import requests

BASE="http://127.0.0.1:5000/"


# response = requests.get(BASE + "startup")
value = "hot"
response = requests.put(BASE + "search", json={"search": value})

print(response.json())
