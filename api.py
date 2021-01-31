
from flask import Flask, request, jsonify
# from flask_cors import CORS

import engine

app = Flask(__name__)
# CORS(app)


@app.route("/api/predict", methods=['POST'])
def predict():
    text = request.json["text"]
    try:
        e = engine(text["command"])
        command = e.get_command()
        entity = e.get_entity(text["entities"])
        return jsonify({
            "command": command,
            "target": entity})
    except Exception as e:
        print(e)
        return jsonify({"result": "Model Failed"})


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)
