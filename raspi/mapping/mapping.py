
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
    
    for i in range(len(mapping)):
        if i == 0 or i == len(mapping)-1:
            continue
        if mapping[i]["note"] == mapping[i-1]["note"] and mapping[i]["note"] == mapping[i+1]["note"]:
            if mapping[i+1]["time"] < 0.05 and mapping[i+1]["time"] > 0:
                delta_time = 0.05 - mapping[i+1]["time"]
                mapping[i+1]["time"] += delta_time
                mapping[i]["time"] -= delta_time/2
                mapping[i+2]["time"] -= delta_time/2

    return mapping