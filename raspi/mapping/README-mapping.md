# install dependencies to run Mapping.py
pip install mido

# Running Mapping.py
## (this will only run the code in 'if __name__ == "__main__": block')
python3 Mapping.py

# midi notes
midi note_on message format:
1001nnnn 0kkkkkkk 0vvvvvvv
where 1001 = note on message, k = which key to press (21 - 108 are the 88 keys on piano), and v = velocity (how hard to press each key)
The mido package calculates the time between each key press for us.

fastest pressing time (based on fastest time in Rush E): 0.0011558666666666667 seconds

## TODO:
- Remove unecessary messages from mido's object
- re-format each message to a new type that only includes necessary information to play song (i.e., channel, key, velocity, time)