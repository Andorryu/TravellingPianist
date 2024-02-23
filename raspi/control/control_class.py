import RPi.GPIO as GPIO
from time import sleep
import json
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


class Control:
    # ______________________________BOARD INITIALIZATION_____________________________________
    # initialize pins on pcf boards
    def init_chip_pins(self) -> list[pcf.PCF]:
        self.num_chips =  math.ceil(self.num_pins/8) # number of pcf boards to use

        #chips = [pcf.PCF(i) for i in range(0x20, 0x20+(8 if num_chips > 8 else num_chips))]
        chips = []
        for i in range(0x20, 0x20+(8 if self.num_chips > 8 else self.num_chips)):
            chips.append(pcf.PCF(i))

        for chip in chips:
            chip.set_i2cBus(1)

        # remainder chips if they exist
        if self.num_chips > 8:
            temp = [pcf.PCF(i) for i in range(0x20, 0x20+(self.num_chips-8))]
            for chip in temp:
                chip.set_i2cBus(2)
            chips += temp

        # init pins
        for i in range(self.num_pins): # create pins "0", "1", ..., f"{num_pins-1}"
            print(f"assigning pinmode {i}")
            chips[(i//8)].pin_mode(f"{i%8}", "OUTPUT")
            print(f"assigned pinmode {i}")

        for i in range(self.num_pins):
            chips[(i//8)].write(f"p{i%8}", "LOW")
        return chips

        # example chips and their associated pins for num_pins = 24:
        # chips[0] -> "0", "1", "2", "3", "4", "5", "6", "7"
        # chips[1] -> "8", "9", "10", "11", "12", "13", "14", "15"
        # chips[2] -> "16", "17", "18", "19", "20", "21", "22", "23"


    def init_pi_pins(self) -> None:
        if self.num_pins > MAX_PI_PINS:
            raise Exception("num_pins is too high/not enough pins on the Pi")
        GPIO.setmode(GPIO.BCM)
        for i in range(self.num_pins):
            GPIO.setup(PI_PIN_MAP[i], GPIO.OUT)


    def init_pins(self):
        match self.mode.upper():
            case "PI":
                return self.init_pi_pins(self.num_pins, self.offset)
            case "I2C":
                return self.init_chip_pins(self.num_pins, self.offset)
    # _______________________________________________________________________________________

    def __init__(self, json_path, mode="I2C", num_pins=88, offset=0):
        self.mode = mode
        self.num_pins = num_pins
        self.offset = offset
    
        file = open(json_path, "r")
        json_data = file.read()
        file.close()
        self.song_data = json.loads(json_path)

        # raspi initialization "stuff"
        self.pins = self.init_pins(self.num_pins, self.offset, self.mode)
        
        # should probably check that initialization passes here

    
    # high_low: "HIGH" or "LOW"
    def note_event_i2c(self, chips: list[pcf.PCF], note_code, high_low: str):
        chips[note_code//8].write(f"{note_code%8}", high_low)


    # high_low: "HIGH" or "LOW"
    def note_event_pi(self, note_code, on_off: bool):
        GPIO.output(PI_PIN_MAP[note_code], on_off)


    def do_note_event(self, offset, num_pins, mode, pins, note_code, on):
        if note_code >= self.offset and note_code < self.offset + self.num_pins:# in range
            match self.mode:
                case "PI":
                    note_event_pi(note_code, on)
                case "I2C":
                    note_event_i2c(pins, note_code, "HIGH" if on else "LOW")
            print(f"pressed note {note_code} {'on' if on else 'off'}")


    def check_song_data(self):
        if len(self.song_data):
            return True
        else:
            return False


    def play_song(self):
        # loop through each note event
        for note_event in song_data:
            # collect note event data
            note = note_event["note"]
            vel = note_event["velocity"]
            time = note_event["time"]

            sleep(time)

            # add PWM control here in later version
            if vel > 0: # note on
                do_note_event(self.offset, self.num_pins, self.mode, self.pins, note, True)
            else: # note off
                do_note_event(self.offset, self.num_pins, self.mode, self.pins, note, False)

        GPIO.cleanup()