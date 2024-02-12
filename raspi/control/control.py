
import RPi.GPIO as GPIO
from time import sleep
import math
import sys
import pcf8574_io as pcf

MAX_PI_PINS = 28
PI_PIN_MAP = [
    27, # GPIO 0 (ID_SD)
    28, # GPIO 1 (ID_SC)
    3, # GPIO 2 (SDA)
    5, # GPIO 3 (SCL)
    7, # GPIO 4 (GPCLK0)
    29, # GPIO 5
    31, # GPIO 6
    26, # GPIO 7 (CE1)
    24, # GPIO 8 (CE0)
    21, # GPIO 9 (MISO)
    19, # GPIO 10 (MOSI)
    23, # GPIO 11 (SCLK)
    32, # GPIO 12 (PWM0)
    33, # GPIO 13 (PWM1)
    8, # GPIO 14 (TXD)
    10, # GPIO 15 (RXD)
    36, # GPIO 16
    11, # GPIO 17
    12, # GPIO 18 (PCM_CLK)
    35, # GPIO 19 (PCM_FS)
    38, # GPIO 20 (PCM_DIN)
    40, # GPIO 21 (PCM_DOUT)
    15, # GPIO 22
    16, # GPIO 23
    18, # GPIO 24
    22, # GPIO 25
    37, # GPIO 26
    13 # GPIO 27
]

def chip_test():
    pass

# initialize pins on pcf boards
def init_chip_pins(num_pins, offset) -> list[pcf.PCF]:
    num_chips =  math.ceil(num_pins/8) # number of pcf boards to use

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
    for i in range(num_pins): # create pins "0", "1", ..., f"{num_pins-1}"
        chips[i//8].pin_mode(f"{i}", "OUTPUT")
    return chips

    # example chips and their associated pins for num_pins = 24:
    # chips[0] -> "0", "1", "2", "3", "4", "5", "6", "7"
    # chips[1] -> "8", "9", "10", "11", "12", "13", "14", "15"
    # chips[2] -> "16", "17", "18", "19", "20", "21", "22", "23"

def init_pi_pins(num_pins, offset) -> None:
    if num_pins > MAX_PI_PINS:
        raise Exception("num_pins is too high/not enough pins on the Pi")
    GPIO.setmode(GPIO.BCM)
    for i in range(num_pins):
        GPIO.setup(PI_PIN_MAP[i], GPIO.OUT)

def init_pins(num_pins, offset, mode: str):
    match mode.upper():
        case "PI":
            return init_pi_pins(num_pins, offset)
        case "I2C":
            return init_chip_pins(num_pins, offset)

# high_low: "HIGH" or "LOW"
def note_event_i2c(chips: list[pcf.PCF], note_code, high_low: str):
    chips[note_code//8].write(f"{note_code}", high_low)

# high_low: "HIGH" or "LOW"
def note_event_pi(note_code, on_off: bool):
    GPIO.output(PI_PIN_MAP[note_code], on_off)

def note_event(offset, num_pins, mode, pins, note_code, on):
    if note_code >= offset and note_code < offset+num_pins:# in range
        match mode:
            case "PI":
                note_event_pi(note_code, on)
            case "I2C":
                note_event_i2c(pins, note_code, "HIGH" if on else "LOW")
        print(f"pressed note {note_code} {'on' if on else 'off'}")

# mode: "PI" or "I2C"
def play_song(song_data, mode, num_pins=88, offset=0):
    pins = init_pins(num_pins, offset, mode)

    # loop through each note event
    for note_event in song_data:
        # collect note event data
        note = note_event["note"]
        vel = note_event["velocity"]
        time = note_event["time"]

        sleep(time)

        if vel > 0: # note on
            note_event(offset, num_pins, mode, pins, note, True)
        else: # note off
            note_event(offset, num_pins, mode, pins, note, False)

    GPIO.cleanup()

# testing
if __name__ == "__main__":
    import json

    if len(sys.argv) != 5:
        print("Command Format: python3 control.py json_song_file mode num_pins offset")
    else:
        file = open(sys.argv[1], "r")
        json_data = file.read()
        file.close()
        song_data = json.loads(json_data)
        play_song(song_data, sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    
