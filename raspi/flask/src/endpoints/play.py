from flask_restful import Resource
import sys
sys.path.insert(0, '../../')
from control.control_class import Control


json_dir = "/home/will/MIDI/"
json_name = "mid2jsn.json"
json_path = json_dir + json_name


# endpoint 4 -> play song on device
class Play(Resource):
    def get(self):
        # initializing pi board 
        pi_control = Control(json_path)

        # sent to frontend for acknowledgment
        response = {}

        # # checking song was parsed correctly
        # if (pi_control.check_song()):
        #     response['state'] = "True"
        #     pi_board.play_song() # START THIS FUNCTION IN BACKGROUND
        #     # HOW DO WE KNOW WHEN SONG IS DONE (frontend needs update)
        # else:
        #     response['state'] = "False"

        response['state'] = "True"

        return response, 200