## IN FLASK.... PUT REQUEST CAN CONTAIN ATTACHED JSON DATA
# WHILE GET REQUESTS CANNOT!

import requests

# local base url of flask server
# host='127.0.0.1'  port='5000'
BASE="http://127.0.0.1:5000/"



##################################################################
# # testing endpoint 1 -> "/startup"
def startup():
	response = requests.get(BASE + "startup")
	print(response.json())



##################################################################
# # testing endpoint 2 -> "/search"
def search():
	value = "hot"
	response = requests.put(BASE + "search", json={"search": value})
	print(response.json())



##################################################################
# # testing endpoint 3 -> "/upload"
def upload():
	value = "Hotline_Bling.mid"
	response = requests.put(BASE + "upload", json={"name": value})
	print(response.json())



###################################################################
# # testing endpoint 4 -> "/play"
def play():
	response = requests.get(BASE + "play")
	print(response.json())



##################################################################
# # testing endpoint 5 -> "/reset"
def reset():
	response = requests.put(BASE + "play", json={})
	print(response.json())
	
	
	
def main():
	print("Enter a endpoint number\n")
	print("startup -> 1\nsearch  -> 2\nupload  -> 3\nplay    -> 4\nreset   -> 5\n")
	user_input = 9
	while user_input !=  0:
		user_input = int(input())
		if user_input == 1:
			print("/startup\n")
			startup()
		elif user_input == 2:
			print("/search\n")
			search()
		elif user_input == 3:
			print("/upload\n")
			upload()
		elif user_input == 4:
			print("/play\n")
			play()
		elif user_input == 5:
			print("/reset\n")
			reset()
		else:
			print("Not a valid input\n")
			user_input = 9
			
main()





