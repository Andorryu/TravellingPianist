
import mido

timeline = list[dict]

"""
    file: midifile filename
"""
def Map(file) -> timeline:
    raw_data = mido.MidiFile(file)
    mapping: timeline = []
    delta_time: int = 0

    # for every midi message
    for msg in raw_data:
        msg_dict = msg.dict()
        msg_type = msg_dict["type"]

        # if not a note event message, increment delta_time
        if msg_type != "note_on" and msg_type != "note_off":
            delta_time += msg_dict["time"]
            continue

        msg_note = msg_dict["note"] - 21
        msg_vel = msg_dict["velocity"]
        msg_time = msg_dict["time"] + delta_time

        new_note_event: dict = {
            "note": msg_note,
            "velocity": msg_vel,
            "time": msg_time
        }

        delta_time = 0
        mapping.append(new_note_event)

    return mapping

# TESTING -------------------------------------------------------------------------------------------------

import sys
import math
import time
import os
import signal

def play_song(mapping: timeline):
    s = Session(max_threads=10000) # high number of threads so that rush e can play lmao
    piano = s.new_part("piano")
    proc_dict: dict[int, Clock] = {}
    for event in mapping:
        if event["time"] > 0:
            time.sleep(event["time"])
        if event["velocity"] > 0:
            clock = fork(piano.play_note, [event["note"]+21, event["velocity"]/127, 100])
            # cache clock
            proc_dict[event["note"]] = clock
        else:
            for note in proc_dict:
                if note == event["note"]:
                    proc_dict[note].kill()

if __name__ == "__main__":
    from scamp import *

    # interpret command-line
    if len(sys.argv) != 2:
        print(f"Command format: python3 mapping.py [path-to-file]")

    # do mapping
    mapping = Map(sys.argv[1])

    # write note details to file
    file = open(f"{sys.argv[1]}-output.txt", "w")
    for msg in mapping:
        file.write(str(msg) + "\n")
    file.close()

    # play song thru unit test function
    print("Playing song...")
    play_song(mapping)
