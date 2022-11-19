import json

from flask import Flask
from flask_restful import Resource, Api, reqparse
from repository import Repository
from volunteer import Volunteer


app = Flask("my_server")
rest_api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('city', type=str, help='', location='args')

repository = Repository(["Warsaw", "Krakow"], [Volunteer("A", "Tokyo"), Volunteer("B", "Warsaw")])


class Cities(Resource):

    def get(self):
        return repository.cities


class Volunteers(Resource):

    def get(self):
        data = parser.parse_args()
        print(data)
        if "city" in data:
            return repository.get_volunteers_by_city(data.get("city"))


if __name__ == "__main__":
    rest_api.add_resource(Cities, '/api/getCities')
    rest_api.add_resource(Volunteers, '/api/getVolunteers')
    app.run(host="localhost", port=8888, debug=True)

