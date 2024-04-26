
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
        delta_time = 0
        current_note = mapping[i]["note"]
        for j in range(i+1, len(mapping)):
            delta_time += mapping[j]["time"]
            if current_note == mapping[j]["note"]:
                if delta_time < 0.05:
                    for k in range(j, i, -1): # search backwards for first instance of non-zero time

                        if mapping[k]["time"] > 0:
                            mapping[k]["time"] = 0.05
                            break
                break

    return mapping

# testing
if __name__ == "__main__":
    pass
