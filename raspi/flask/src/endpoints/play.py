from flask_restful import Resource
import sys
sys.path.insert(0, '../../')
from control.control_class import Control


json_dir = "/home/will/MIDI"
json_name = "midi2jsn.json"
json_path = midi_dir + midi_name


# endpoint 4 -> play song on device
class Play(Resource):
    def get(self):
        # initializing pi board 
        pi_board = Control(json_path)

        # validating initialization
        response = {}
        if (pi_board.check_song_data):
            response['state'] = "True"
            pi_board.play_song()
            return response, 200
        else:
            response['state'] = "False"
            return response, 400