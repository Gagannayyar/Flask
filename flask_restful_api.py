
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkdata(postedData, functionname):
    if (functionname == 'add' or functionname == 'substract' or functionname == 'multiply'):
        if "x" not in postedData or "y" not in postedData:
            return 301 #missing data
        else:
            return 200 #success
    elif (functionname == 'divide'):
        #special case of divide with zero in divide
        if "x" not in postedData or "y" not in postedData:
            return 301 #missing data
        elif int(postedData["y"]) == 0:
            return 302 #divide with zero
        else:
            return 200 # success



class Add(Resource):
    def post(self):
        #get posted data
        postedData = request.get_json()
        #get status code
        status_code = checkdata(postedData=postedData, functionname='add')

        if (status_code != 200):

            retjson = {
                "Error": "Missing data",
                "Status": status_code
            }
            return jsonify(retjson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            z = x+y
            retjson = {
                "Sum": z,
                "Status Code": status_code
            }
            return jsonify(retjson)


class Substract(Resource):
    def post(self):
        #get posted data
        postedData = request.get_json()
        #get status code
        status_code = checkdata(postedData=postedData, functionname='substract')

        if (status_code != 200):

            retjson = {
                "Error": "Missing data",
                "Status": status_code
            }
            return jsonify(retjson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            z = x-y
            retjson = {
                "Message": z,
                "Status Code": status_code
            }
            return jsonify(retjson)

class Divide(Resource):
    def post(self):
        #get posted data
        postedData = request.get_json()
        #get status code
        status_code = checkdata(postedData=postedData, functionname='divide')

        if (status_code != 200):

            retjson = {
                "Error": "Missing data",
                "Status": status_code
            }
            return jsonify(retjson)
        
        elif (status_code == 302):
            retjson = {
                "Error": "Cannot divide with zero",
                "Status": status_code
            }
            return jsonify(retjson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            z = x/y
            retjson = {
                "Sum": z,
                "Status Code": status_code
            }
            return jsonify(retjson)

class Multiply(Resource):
    def post(self):
        #get posted data
        postedData = request.get_json()
        #get status code
        status_code = checkdata(postedData=postedData, functionname='multiply')

        if (status_code != 200):

            retjson = {
                "Error": "Missing data",
                "Status": status_code
            }
            return jsonify(retjson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)
            z = x*y
            retjson = {
                "Sum": z,
                "Status Code": status_code
            }
            return jsonify(retjson)


api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def hello():
    return "Hello"


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

