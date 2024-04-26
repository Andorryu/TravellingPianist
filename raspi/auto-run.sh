#!/bin/bash

# activate python virtual enviroment
source ../venv/bin/activate

lxterminal --command=" bash -c 'cd /home/piano/TravellingPianist/raspi/flask; sudo python3 src/main.py; exec bash'" &
lxterminal --command=" bash -c 'cd /home/piano/TravellingPianist/raspi/react; npm start; exec bash'"



