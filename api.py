from flask import Flask, request, jsonify

# from flask_cors import CORS

from engine import engine

app = Flask(__name__)
# CORS(app)


@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        e = engine(request.json["command"])
        command = e.get_command()
        entity = e.get_entity(request.json["entities"], request.json["command"])
        return jsonify({"command": command, "target": entity})
    except Exception as e:
        print(e)
        return jsonify({"result": "Model Failed"})


if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)
