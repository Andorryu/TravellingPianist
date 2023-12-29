from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

import os

from chromedriver import ChromeDriver


# CHANGE ON RASPI PLATFORM
downloads_path = "/home/will/Downloads"

def update_list(search_value):
    song_response_list = []
    files = os.listdir(downloads_path)
    for file in files:
        if search_value.lower() in file.lower():
        # # better search... keep improving
        # if search_value.lower() in file.lower().split(".")[0]:
            song_response_list.append(file)
    return song_response_list


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
    
# endpoint 1 -> start up musescore page via selenium call
class StartUp(Resource):
    def get(self):
        musescore_driver = ChromeDriver()
        musescore_driver.run()
        # NEED TO ADD LOCAL BROWSER SIZING IN REACT
        return "", 201
    
# endpoint 2 -> pulling local XML files for search bar
search_get_args = reqparse.RequestParser()
search_get_args.add_argument("search", type=str, help="Flask search not valid...")

class Search(Resource):
    def put(self):
        args = search_get_args.parse_args()
        song_name = args["search"]
        song_response_list = update_list(song_name)

        song_response_dicts = []
        id = 0
        for song in song_response_list:
            song_dict = {}
            song_dict['id'] = id
            song_dict['name'] = song
            id += 1
            song_response_dicts.append(song_dict)
        return song_response_dicts, 200



api.add_resource(StartUp, "/startup")
api.add_resource(Search, "/search")

if __name__ == "__main__":
    # change debug to false once ready for production
    app.run(debug=True)