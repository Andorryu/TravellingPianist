import configparser

config = configparser.ConfigParser()

config.read('/home/will/Desktop/config.ini')

username = config['credentials']['username']
password = config['credentials']['password']


