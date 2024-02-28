
import RPi.GPIO as GPIO
from time import sleep
import math
import sys
import pcf8574_io as pcf
import json

class Control:
    def __init__(self, json_path, num_keys=88, offset=0):
        self.offset = offset
        self.song_data = parse_json(json_path)
        
        num_chips =  math.ceil(num_keys/8) # number of pcf boards to use

        chips = [pcf.PCF(i) for i in range(0x20, 0x20+(8 if num_chips > 8 else num_chips))]

        for chip in chips:
            chip.set_i2cBus(1)

        # remainder chips if they exist
        if num_chips > 8:
            temp = [pcf.PCF(i) for i in range(0x20, 0x20+(num_chips-8))]
            for chip in temp:
                chip.set_i2cBus(2)
            chips += temp

        # init pins
        for i in range(num_keys): # create pins "0", "1", ..., f"{num_pins-1}"
            chips[(i//8)].pin_mode(f"{i%8}", "OUTPUT")

        for i in range(num_keys):
            chips[(i//8)].write(f"p{i%8}", "LOW")

        self.chips = chips
        
        if (self.check_song()):
            print("INIT PASSED SUCCESFULLY\n")
        else:
            print("INIT FAILED\n")

    def parse_json(json_path):
        file = open(json_path, "r")
        json_data = file.read()
        file.close()
        return json_data

    def check_song():
        if len(self.song_data) > 0:
            return True
        else:
            return False
    
    # high_low: "HIGH" or "LOW"
    def output(self, note, high_low: str):
        note -= self.offset
        self.chips[note//8].write(f"{note%8}", high_low)

    def play_song(self):
        for note_event in self.song_data:
            note = note_event["note"]
            vel = note_event["velocity"]
            time = note_event["time"]

            sleep(time)

            self.output(note, "HIGH" if vel > 0 else "LOW")


# testing
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Command Format: python3 control.py <json_path> <num_pins> <offset>")

    else:
        con = Control(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])) # initialize
        con.play_song() # play song
