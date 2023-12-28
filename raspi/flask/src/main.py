from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

import os

from chromedriver import ChromeDriver


# CHANGE ON RASPI PLATFORM
downloads_path = "/home/will/Downloads"

songs_dict = {}

# update song dictionary with new downloaded songs
def update_dict():
    files = os.listdir(downloads_path)

    for file in files:
        if len(songs_dict) == 0:
            songs_dict[0] = file
        elif file in songs_dict.values():
            pass
        else:
            songs_dict[list(songs_dict.keys())[-1]+1] = file


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
        update_dict()

        args = search_get_args.parse_args()
        song_name = args["search"]
        
        # probably will have to update searching capabilities later... only looks for similar inline letters
        filtered_dict = {key: value for key, value in songs_dict.items() if song_name.lower() in value.lower().split(".")[0]}
        
        return filtered_dict, 200



api.add_resource(StartUp, "/startup")
api.add_resource(Search, "/search")

if __name__ == "__main__":
    # change debug to false once ready for production
    app.run(debug=True)