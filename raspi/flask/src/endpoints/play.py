from flask_restful import Resource

# endpoint 4 -> play song on device
class Play(Resource):
    def get(self):
        response = {}

        if 1 == 2:
            response["state"] = "True"
        else:
            response["state"] = "False"

        return response, 200