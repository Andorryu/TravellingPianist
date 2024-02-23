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
