#!/bin/bash

# activate python virtual enviroment
source ./venv/bin/activate

# start up flask server
gnome-terminal -- bash -c "cd /home/will/TravellingPianist/raspi/flask; sudo python3 src/main.py; exec bash"

# start up test menu script
gnome-terminal -- bash -c "cd /home/will/TravellingPianist/raspi/flask; python3 test/test_1py; exec bash"


python3 /home/will/TravellingPianist/raspi/flask/test/test_1.py 

