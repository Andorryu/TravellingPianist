from flask_restful import Resource, reqparse
import os

downloads_path = '/home/will/Downloads'

def find_song(song_name):
    files = os.listdir(downloads_path)

    if song_name not in files:
        return False
    else:
        return downloads_path + song_name


upload_put_args = reqparse.RequestParser()
upload_put_args.add_argument("name", type=str, help="Not a string song name...")

# endpoint 3 -> upload user selected file to device
class Upload(Resource):
    def put(self):
        args = upload_put_args.parse_args()
        song_name = args["name"]
        song_path = find_song(song_name)

        response = {}
        if song_path == False:
            # checking if any song is selected
            response["state"] = "No Song Selected"
        elif 1 == 2:
            # wait and check for valid upload
            response["state"] = "False"
        else:
            response["state"] = "True"
        return response, 200