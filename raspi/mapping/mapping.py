
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
            "time": msg_time + (0 if msg_time == 0 else 0.05)
        }

        delta_time = 0
        mapping.append(new_note_event)

    return mapping