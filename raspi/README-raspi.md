# Installing React Project on Pi OS

## 1. Project Dependencies

### Update Kernel
sudo apt update

### Install Git for version control and cloning
sudo apt install git

### Install Node.js
sudo apt install nodejs

### Install npm (Node Package Manager)
sudo apt install npm

### Install curl
sudo apt install curl

### Install NVM (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash

### Commit NVM Install
source ~/.bashrc


## 2. Launching Project

### Pull from remote repository 
git clone https://github.com/Andorryu/TravellingPianist.git

### Navigate to project repository
cd raspi/react

### Install project dependecies located in package.json
npm install

### Launch the Web Server
npm start


# Installing Flask Project on Pi OS

## 1. Install Project Dependencies

### Activate virtual enviroment
sudo apt install python3-venv
source bin/activate

### Download required python packages
pip install -r requirements.txt


## 2. Install ChromeDriver

### Download chromedriver from 
https://googlechromelabs.github.io/chrome-for-testing/

### Extract executable and place in /usr/bin/chromedriver
sudo mv chromedriver /usr/bin/chromedriver


# Running the "Servers"

## 1. Booting React

### Launch the local react web app from its project folder
npm start


### 2. Booting Flask

### Launch the local flash api from its project folder
python3 src/main.py


### autorun dependencies
sudo apt-get install xdotool







