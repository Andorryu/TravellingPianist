# install dependencies to run Mapping.py
pip install mido

# Running Mapping.py
## (this will only run the code in 'if __name__ == "__main__": block')
python3 Mapping.py

# midi notes
midi note_on message format:
1001nnnn 0kkkkkkk 0vvvvvvv
where 1001 = "note on" message, n = which channel to play note on, k = which key to press (21 - 108 are the 88 keys on piano), and v = velocity (how hard to press each key)
The mido package calculates the time between each key press for us.

fastest pressing time in Rush E: 0.0011546666666666665 seconds
fastest pressing time in Comptine_Dun_Autre_t_-_Yann_Tiersen: 0.0012499979166666665 seconds

# MuseScore midi simplifications (assertions) (pls test these)
note_on with 0 velocity is used to unpress every key sometimes
when note_off is used instead, it seems to have velocity of 0 anyways
