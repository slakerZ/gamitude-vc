from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from flask_cors import CORS

from engine import engine

app = Flask(__name__)
api = Api(app)
CORS(app)


class Prediction(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "command", help="Need command to recognize intentions", required=True, type=str
    )
    parser.add_argument(
        "entities",
        help="Please provide object containing projects, folders and timers lists",
        required=True,
        type=dict
    )

    def post(self):
        data = Prediction.parser.parse_args()
        e = engine(data["command"])
        print(data)
        entities = data["entities"]
       
        command = e.get_command()
        entity = e.get_entity_id(entities, command)
        return {"command": command, "target": entity}, 200


api.add_resource(Prediction, "/api/predict")
