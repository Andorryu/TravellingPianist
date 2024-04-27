from flask_restful import Resource
import sys
from multiprocessing import Process
import os
import signal
sys.path.insert(0, '../')
from control.control import Control


json_dir = "/home/piano/MIDI/"
json_name = "mid2jsn.json"
#json_name = "beat.json"
json_path = json_dir + json_name

PID = None


# endpoint 4 -> play song on device
class Play(Resource):
    def __init__(self):
        super().__init__()
        self.con = Control(num_keys=64, offset=0)

    def play_song_process(self, json_path):
        self.con.play_song(json_path)

    def get(self):
        # prepare the response
        response = {'state': "True"}

        p = Process(target=self.play_song_process, args=(json_path,))
        p.start()

        global PID
        PID = p.pid

        print(f"Play Song PID: {p.pid}\n\n")

        return response, 200
    
    def put(self):
        # args = upload_put_args.parse_args()

        # prepare the response
        response = {"state": "True"}

        # set all pins to 0V
        self.con.reset_pins()
        global PID
        print(f"Play Song PID: {PID}\n\n")

        # kill play_song_process process via PID
        if PID != None:
            os.kill(PID, signal.SIGTERM)

        return response, 200