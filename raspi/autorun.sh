#!/bin/bash

# WORK IN PROGRESS ----> PROBABLY SHOULD BE PUSHED TO A MAKEFILE LATER
# # autorun dependencies
# sudo apt-get install xdotool

# RUN VIA THE FOLLOWING COMMAND: ./autorun.sh

gnome-terminal -- bash -c "cd /home/will/TravellingPianist/; source ./venv/bin/activate; cd raspi/flask; python3 src/main.py; exec bash"

gnome-terminal -- bash -c "cd /home/will/TravellingPianist; source ./venv/bin/activate; cd raspi/react; npm start; exec bash"


wait 3

# Get the window ID of the Chrome window
chrome_window_id=$(xdotool search --name "Chromium Web Browser" | head -n 1)

# Check if the Chrome window ID is found
if [ -n "$chrome_window_id" ]; then
    # Resize the Chrome window
    xdotool windowsize "$chrome_window_id" 800 600
    echo "Chrome window resized to 800x600"
else
    echo "Chrome window not found"
fi

# starting musescore side bar
curl -s "http://127.0.0.1:5000/startup"


