from flask_restful import Resource
import sys
sys.path.insert(0, '../')
from control.control import Control


json_dir = "/home/will/MIDI/"
# json_name = "mid2jsn.json"
json_name = "beat.json"
json_path = json_dir + json_name


# endpoint 4 -> play song on device
class Play(Resource):
    def get(self):
        # initializing pi board 
        pi_control = Control(json_path=json_path, num_keys=4, offset=0)

        # sent to frontend for acknowledgment
        response = {}

        # # checking song was parsed correctly
        # if (pi_control.check_song()):
        #     response['state'] = "True"
        #     pi_control.play_song() # START THIS FUNCTION IN BACKGROUND
        #     # HOW DO WE KNOW WHEN SONG IS DONE (frontend needs update)
        # else:
        #     response['state'] = "False"
        pi_control.play_song()

        return response, 200