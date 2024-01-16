
import mido

# define type aliases
key_event = dict[str, int]
score = list[key_event]

"""
    file: string that represents the relative file location of the midi file
    returns a score that represents the data to be transmitted to the arduino
"""
def Map(file) -> score:
    raw_data = mido.MidiFile(file)
    mapping: score = []
    delta_time: int = 0

    # for every midi message
    for msg in raw_data:
        msg_dict = msg.dict()
        msg_type = msg_dict["type"]

        # if not a note event message, increment delta_time
        if msg_type != "note_on" and msg_type != "note_off":
            delta_time += msg_dict["time"]
            continue

        msg_chan = msg_dict["channel"]
        msg_note = msg_dict["note"]
        msg_vel = msg_dict["velocity"]
        msg_time = msg_dict["time"] + delta_time

        new_key_event: key_event = {
            #"type": msg_type,
            #"channel": msg_chan,
            "note": msg_note,
            "velocity": msg_vel,
            "time": msg_time
        }

        delta_time = 0
        mapping.append(new_key_event)

    return mapping


# TESTING -------------------------------------------------------------------------------------------------

import sys
import pysine
import math
import time

def play_song(mapping: score):
    for event in mapping:
        if event["velocity"] > 0:
            pysine.sine(2**((event["note"]-21)/12)*27.5, event["time"])
        else:
            time.sleep(event["time"])

if __name__ == "__main__":
    

    # interpret command
    if len(sys.argv) != 2:
        print(f"Command format: python3 mapping.py [path-to-file]")

    # write note details to file and print fastest pressing time
    file = open(f"{sys.argv[1]}-output.txt", "w")
    mapping = Map(sys.argv[1])
    times = []
    for msg in mapping:
        if msg["time"] != 0:
            times.append(msg["time"])
        file.write(str(msg) + "\n")
    file.close()

    print(f"Fastest pressing time: {min(times)}")

    print("Playing song...")
    play_song(mapping)

