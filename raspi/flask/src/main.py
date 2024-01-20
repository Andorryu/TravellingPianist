from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from endpoints.startup import StartUp
from endpoints.search import Search
from endpoints.upload import Upload
from endpoints.play import Play
from endpoints.reset import Reset



app = Flask(__name__)
api = Api(app)
cors = CORS(app)
    

api.add_resource(StartUp, "/startup")
api.add_resource(Search, "/search")
api.add_resource(Upload, "/upload")
api.add_resource(Play, "/play")
api.add_resource(Reset, "/reset")


if __name__ == "__main__":
    # change debug to false once ready for production
    app.run(debug=True, host="127.0.0.1", port="5000")