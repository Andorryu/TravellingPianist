from flask_restful import Resource

# endpoint 5 -> full device hard reset (not web server only queue software)
class Reset(Resource):
    def get(self):
        response = {}

        if 1 == 2:
            response["state"] = "True"
        else:
            response["state"] = "False"

        return response, 200