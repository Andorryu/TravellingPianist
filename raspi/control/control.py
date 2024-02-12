
import RPi.GPIO as GPIO
from time import sleep
import math
import pcf8574_io as pcf

def chip_test():
    pass

def init_pins() -> list[pcf.PCF]:
    num_pins = 12 # aka number of keys on piano that we are using
    offset = 0 # when not using all 88 keys, how far up the piano board should we play?
    num_chips =  math.ceil(num_pins/8)
    # create PCF objects - this can handle up to 64 pins
    chips = [pcf.PCF(i) for i in range(0x20, 0x20+num_chips)]
    # init pins
    for i in range(num_pins): # create pins "0", "1", ..., f"{num_pins-1}"
        chips[i//8].pin_mode(f"{i}", "OUTPUT")
    return chips

    # example chips and their associated pins for num_pins = 24:
    # chips[0] -> "0", "1", "2", "3", "4", "5", "6", "7"
    # chips[1] -> "8", "9", "10", "11", "12", "13", "14", "15"
    # chips[2] -> "16", "17", "18", "19", "20", "21", "22", "23"


def play_note(note_code):
    global chips
    chips[note_code//8].write(f"{note_code}", "HIGH")

def stop_note(note_code):
    global chips
    chips[note_code//8].write(f"{note_code}", "LOW")

def play_song(song_data):
    
    pins = init_pins()

    # loop through each note event
    for note_event in song_data:
        # collect note event data
        note = note_event["note"]
        vel = note_event["velocity"]
        time = note_event["time"]

        sleep(time)

        if vel > 0: # note on
            play_note(note)
        else: # note off
            stop_note(note)

# module initialization
GPIO.setmode(GPIO.BOARD)
chips = init_pins()

# testing
if __name__ == "__main__":
    pass
