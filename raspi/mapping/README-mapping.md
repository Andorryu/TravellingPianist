
# DEPENDENCIES
## dependencies to run Map() function
pip install mido
## dependecies for running unit test
sudo apt install fluidsynth
pip install scamp

# Running Mapping.py
python3 Mapping.py

# Midi Stuff
midi note_on message format:
1001cccc 0nnnnnnn 0vvvvvvv
where 1001 = "note on" message, c = which channel to play note on, n = which note to play, and v = velocity (how hard to press each key)
- The mido package calculates the time between each key press for us (normally its embedded in the meta messages i think)
- note values 21 - 108 map to the 88 keys on a piano
- a message with velocity 0 means to unpress the key

# TODO
- Better error checking & documentation
