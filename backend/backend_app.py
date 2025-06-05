from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://harshavvc234:wP5Ifcv0FwJuj3vG@cluster444.x7wmqzg.mongodb.net/")
client = MongoClient(MONGO_URI)
db = client["mydb"]
collection = db["mycollection"]

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        if not all(k in data for k in ("name", "email", "age", "country")):
            return jsonify({"error": "Missing fields"}), 400

        data['age'] = int(data['age'])
        collection.insert_one(data)
        return jsonify({"message": "Success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)

