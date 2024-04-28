
from time import monotonic, sleep
import math
import sys
import pcf8574_io as pcf
import json
import RPi.GPIO as GPIO

# NOTE: FOR OCTAVE TEST, MAKE OFFSET = 39 AND NUM_KEYS = 12

class Control:
    def __init__(self, num_keys=88, offset=0):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.offset = offset
        self.num_keys = num_keys
        num_chips =  8 if num_keys > 64 else math.ceil(num_keys/8) # number of pcf boards to use

        chips = [pcf.PCF(i) for i in range(0x20, 0x20+num_chips)]

        # init pins
        for i in range(64 if num_keys > 64 else num_keys): # create pins "0", "1", ..., f"{num_pins-1}"
            chips[(i//8)].pin_mode(f"{i%8}", "OUTPUT")

        # remainder on gpio pins
        for i in range(4, 28):
            GPIO.setup(i, GPIO.OUT)

        self.chips = chips

    def parse_json(self, json_path):
        file = open(json_path, "r")
        json_data = file.read()
        file.close()
        json_data = json.loads(json_data)
        return json_data

    # high_low: "HIGH" or "LOW"
    def output(self, note, high_low: str):
        note -= self.offset
        #if note < self.num_keys and note >= 0: #skip notes that aren't in window
        if note < 64:
            self.chips[note//8].write(f"{note%8}", high_low)
        elif note < 88:
            GPIO.output(note-60, GPIO.HIGH if high_low == "HIGH" else GPIO.LOW)


    def play_song(self, song_path):
        song_data = self.parse_json(song_path)
        print("Playing song...")
        for note_event in song_data:
            note = note_event["note"]
            vel = note_event["velocity"]
            time = note_event["time"]

            #print(note)

            start = monotonic()
            end = monotonic()
            while end - start < time:
                end = monotonic()
            
            #print(f"Time waited: {end-start} vs time desired: {time}")

            note -= self.offset
            if note < self.num_keys and note >= 0: #skip notes that aren't in window
                self.output(note, "HIGH" if vel > 0 else "LOW")
        print("Song finished")

    def reset_pins(self):
        for i in range(self.num_keys):
            self.output(i, "LOW")


# testing
if __name__ == "__main__":
    con = Control(num_keys=88, offset=0)
    con.reset_pins()
    while True:
        inp = input()
        if inp == "r":
            con.reset_pins()
        elif inp.isnumeric():
            if int(inp) >= 0 and int(inp) < con.num_keys:
                con.output(int(inp), "HIGH")
                sleep(2)
                con.output(int(inp), "LOW")
