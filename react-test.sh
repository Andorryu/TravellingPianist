#!/bin/bash

# activate python virtual enviroment
source ./venv/bin/activate

# starting react server
gnome-terminal -- bash -c "cd /home/will/TravellingPianist/raspi/react; serve -g build; exec bash"

wait 5

# starting flask server in background
python3 /home/will/TravellingPianist/raspi/flask/src/main.py


