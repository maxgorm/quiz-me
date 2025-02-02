from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Allow frontend requests

data_store = "quiz_data.json"

def load_data():
    if os.path.exists(data_store):
        with open(data_store, "r") as file:
            return json.load(file)
    return {"terms": []}

def save_data(data):
    with open(data_store, "w") as file:
        json.dump(data, file, indent=2)

@app.route("/upload", methods=["POST"])
def upload_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        save_data(data)
        return jsonify({"message": "Data successfully uploaded!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/data.json", methods=["GET"])
def get_data():
    data = load_data()
    return jsonify(data), 200

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    # Create static directory if it doesn't exist
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
