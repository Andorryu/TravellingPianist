from flask_restful import Resource
import sys
import os
import signal
sys.path.insert(0, '../')
from control.control import Control


json_dir = "/home/will/MIDI/"
json_name = "mid2jsn.json"
# json_name = "beat.json"
json_path = json_dir + json_name


# endpoint 4 -> play song on device
class Play(Resource):
    def __init__(self):
        super().__init__()
        self.con = Control(num_keys=4, offset=0)
        self.pid = 0

    def get(self):
        # initializing pi board 

        # sent to frontend for acknowledgment
        response = {}

        # # checking song was parsed correctly
        # if (pi_control.check_song()):
        #     response['state'] = "True"
        #     pi_control.play_song() # START THIS FUNCTION IN BACKGROUND
        #     # HOW DO WE KNOW WHEN SONG IS DONE (frontend needs update)
        # else:
        #     response['state'] = "False"
        self.con.play_song(json_path)

        return response, 200
    
    def put(self):
        # args = upload_put_args.parse_args()

        response = {"state": "True"}
        self.con.reset_pins()
        print("PID", os.getpid())
        print("RESET CALLED\n")
        os.kill(os.getpid(), signal.SIGSTOP)

        return response, 200