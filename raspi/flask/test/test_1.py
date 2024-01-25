## IN FLASK.... PUT REQUEST CAN CONTAIN ATTACHED JSON DATA
# WHILE GET REQUESTS CANNOT!

import requests

# local base url of flask server
# host='127.0.0.1'  port='5000'
BASE="http://127.0.0.1:5000/"



##################################################################
# # testing endpoint 1 -> "/startup"
# response = requests.get(BASE + "startup")
# print(response.json())



##################################################################
# # testing endpoint 2 -> "/search"
# value = "hot"
# response = requests.put(BASE + "search", json={"search": value})
# print(response.json())



##################################################################
# testing endpoint 3 -> "/upload"
value = "boh-rap.mid"
response = requests.put(BASE + "upload", json={"name": value})
print(response.json())



###################################################################
# # testing endpoint 4 -> "/play"
# response = requests.get(BASE + "play")
# print(response.json())



##################################################################
# # testing endpoint 5 -> "/reset"
# response = requests.get(BASE + "reset")
# print(response.json())
