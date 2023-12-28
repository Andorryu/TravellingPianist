from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

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
# app.config['CORS_HEADERS'] = "Content-Type"
    
# endpoint 1 -> start up musescore page via selenium call
class StartUp(Resource):
    def get(self):
        musescore_driver = ChromeDriver()
        musescore_driver.run()
        # NEED TO ADD LOCAL BROWSER SIZING IN REACT
        return "", 201
    
# endpoint 2 -> pulling local XML files for search bar
class Search(Resource):
    def get(self, song_name):
        update_dict()
        filtered_dict = {key: value for key, value in songs_dict.items() if song_name.lower() in value.lower()}

        
        return filtered_dict, 200



api.add_resource(StartUp, "/startup")
api.add_resource(Search, "/search/<string:song_name>")

if __name__ == "__main__":
    # change debug to false once ready for production
    app.run(debug=True)