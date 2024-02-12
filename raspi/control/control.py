
import RPi.GPIO as GPIO
from time import sleep
import math
import sys
import pcf8574_io as pcf
import json

class Control:
    def __init__(self, num_keys=88, offset=0):
        self.offset = offset
        self.num_keys = num_keys
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
        self.reset_pins()


    def parse_json(self, json_path):
        file = open(json_path, "r")
        json_data = file.read()
        file.close()
        json_data = json.loads(json_data)
        return json_data

    # high_low: "HIGH" or "LOW"
    def output(self, note, high_low: str):
        
        note -= self.offset
        if note < self.num_keys and note >= 0: #skip notes that aren't in window
            self.chips[note//8].write(f"{note%8}", high_low)

    def play_song(self, song_path):
        song_data = self.parse_json(song_path)
        for note_event in song_data:
            note = note_event["note"]
            vel = note_event["velocity"]
            time = note_event["time"]

            print(note_event['note'])

            sleep(time)

            self.output(note, "HIGH" if vel > 0 else "LOW")

    def reset_pins(self):
        for i in range(self.num_keys):
            self.chips[i//8].write(f"{i%8}", "LOW")


# testing
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Command Format: python3 control.py <json_path> <num_pins> <offset>")

    else:
        con = Control(num_keys=int(sys.argv[2]), offset=sys.argv[3])
        con.play_song(sys.argv[1])
