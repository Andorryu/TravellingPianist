
import mido

class NoteEvent:
    def __init__(self, note, velocity, time) -> None:
        self.note: int = note
        self.velocity: int = velocity
        self.time: float = time
    
    def __str__(self):
        return f"note = {' '*(3-len(str(self.note)))}{self.note}, velocity = {' '*(3-len(str(self.velocity)))}{self.velocity}, time = {self.time}"

timeline = list[NoteEvent]

"""
    file: string that represents the relative file location of the midi file
    returns a score that represents the data to be transmitted to the arduino
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

        msg_note = msg_dict["note"]
        msg_vel = msg_dict["velocity"]
        msg_time = msg_dict["time"] + delta_time

        new_note_event: NoteEvent = NoteEvent(msg_note, msg_vel, msg_time)

        delta_time = 0
        mapping.append(new_note_event)

    return mapping

# TESTING -------------------------------------------------------------------------------------------------

import sys
import math
import time
import os
import signal
from scamp import *

def play_song(mapping: timeline):
    s = Session(max_threads=10000) # high number of threads so that rush e can play lmao
    piano = s.new_part("piano")
    proc_dict: dict[int, Clock] = {}
    for event in mapping:
        if event.time > 0:
            time.sleep(event.time)
        if event.velocity > 0:
            clock = fork(piano.play_note, [event.note, event.velocity/127, 100])
            # cache clock
            proc_dict[event.note] = clock
        else:
            for note in proc_dict:
                if note == event.note:
                    proc_dict[note].kill()

if __name__ == "__main__":

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

