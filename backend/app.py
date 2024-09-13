from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['overlay_db']
overlays_collection = db['overlays']

@app.route('/overlays', methods=['POST'])
def create_overlay():
    data = request.json
    overlay_id = overlays_collection.insert_one(data).inserted_id
    return jsonify({"message": "Overlay created", "id": str(overlay_id)})

if __name__ == '__main__':
    app.run(debug=True)


