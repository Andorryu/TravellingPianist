from flask_restful import Resource
from chromedriver.chromedriver import ChromeDriver

# endpoint 1 -> start up musescore page via selenium call
class StartUp(Resource):
    def get(self):
        musescore_driver = ChromeDriver()
        musescore_driver.run()
        # NEED TO ADD LOCAL BROWSER SIZING IN REACT
        return "", 201