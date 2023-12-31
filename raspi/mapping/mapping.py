import mido

if __name__ == "__main__":
    # vars for midi file names
    comptine = "example_songs/Comptine_Dun_Autre_t_-_Yann_Tiersen.mid"
    rush_e = "example_songs/rush_e_real.mid"

    # write note details to file
    file = open("midi-example.txt", "w")
    midi_file = mido.MidiFile(rush_e) # change filename here
    times = []
    for msg in midi_file:
        file.write(str(msg) + "\n")
        if type(msg) == mido.messages.messages.Message and msg.dict()["time"] != 0: # put time in array if not 0
            times.append(msg.dict()["time"])
    file.close()
    # calculate min time
    print(f"fastest pressing time: {min(times)}")
