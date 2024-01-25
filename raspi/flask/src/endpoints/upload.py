from flask_restful import Resource, reqparse
import os
import mido
import json


downloads_path = '/home/will/Downloads/'

def find_song(song_name):
    files = os.listdir(downloads_path)

    if song_name not in files:
        return False
    else:
        return downloads_path + song_name


upload_put_args = reqparse.RequestParser()
upload_put_args.add_argument("name", type=str, help="Not a string song name...")


"""
    file: string that represents the relative file location of the midi file
    returns a score that represents the data to be transmitted to the arduino
"""


timeline = list[dict]

def Map(file) -> timeline:
    raw_data = mido.MidiFile(file)
    mapping: timeline = []
    delta_time: int = 0

    # for every midi message
    for msg in raw_data:
        msg_dict = msg.dict()
        msg_type = msg_dict["type"]

        # if not a note event message, increment delta_time
        if msg_type != "note_on" and msg_type != "note_off":
            delta_time += msg_dict["time"]
            continue

        msg_note = msg_dict["note"]
        msg_vel = msg_dict["velocity"]
        msg_time = msg_dict["time"] + delta_time

        new_note_event: dict = {
            "note": msg_note,
            "velocity": msg_vel,
            "time": msg_time
        }

        delta_time = 0
        mapping.append(new_note_event)

    return mapping


# endpoint 3 -> upload user selected file to device
class Upload(Resource):
    def put(self):
        args = upload_put_args.parse_args()
        song_name = args["name"]
        song_path = find_song(song_name)

        response = {}
        if song_path == False:
            # checking if any song is selected
            # if not return false, button stays red
            response["state"] = "False"
        else:
            mapping = Map(song_path)

            file_name = f'/home/will/MIDI/mid2jsn.json'
            with open(file_name, 'w') as file:
                json.dump(mapping, file, indent=4)

            response["state"] = "True"
        return response, 200