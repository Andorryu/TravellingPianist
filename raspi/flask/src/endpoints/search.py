from flask_restful import Resource, reqparse
import os


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


# endpoint 2 -> pulling local XML files for search bar
search_put_args = reqparse.RequestParser()
search_put_args.add_argument("search", type=str, help="Flask search not valid...")

class Search(Resource):
    def put(self):
        args = search_put_args.parse_args()
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