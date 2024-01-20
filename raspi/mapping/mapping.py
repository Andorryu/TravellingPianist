
import mido

class NoteEvent:
    def __init__(self, channel, note, velocity, time) -> None:
        self.note = note
        self.velocity = velocity
        self.time = time
        self.channel = channel
    
    def __str__(self):
        return f"channel = {self.channel}, note = {' '*(3-len(str(self.note)))}{self.note}, velocity = {' '*(3-len(str(self.velocity)))}{self.velocity}, time = {self.time}"

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

        msg_chan = msg_dict["channel"]
        msg_note = msg_dict["note"]
        msg_vel = msg_dict["velocity"]
        msg_time = msg_dict["time"] + delta_time

        new_note_event: NoteEvent = NoteEvent(msg_chan, msg_note, msg_vel, msg_time)

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
    s = Session()
    piano = s.new_part("piano")
    proc_dict = {}
    for event in mapping:
        if event.time > 0:
            time.sleep(event.time)
        if event.velocity > 0:
            pid = os.fork()
            if pid == 0:
                piano.play_note(event.note, event.velocity/127, 2)
                break
            else:
                # cache pid
                proc_dict[event.note] = pid
        else:
            for note in proc_dict:
                if note == event.note:
                    os.kill(proc_dict[note], signal.SIGTERM)

if __name__ == "__main__":

    # interpret command-line
    if len(sys.argv) != 2:
        print(f"Command format: python3 mapping.py [path-to-file]")

    # write note details to file and print fastest pressing time
    file = open(f"{sys.argv[1]}-output.txt", "w")
    mapping = Map(sys.argv[1])
    times = []
    for msg in mapping:
        if msg.time != 0:
            times.append(msg.time)
        file.write(str(msg) + "\n")
    file.close()

    print(f"Fastest pressing time: {min(times)}")

    print("Playing song...")
    play_song(mapping)

