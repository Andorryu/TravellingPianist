#!/bin/bash

# activate python virtual enviroment
source ./venv/bin/activate

# start up flask server
gnome-terminal -- bash -c "cd /home/will/TravellingPianist/raspi/flask; python3 src/main.py; exec bash"

# start up test menu script
cd /home/will/TrabellingPianist/raspi/flask
python3 test/test_1.py 

