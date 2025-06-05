import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Get MongoDB URI from environment variable or use your Atlas URI as default
MONGO_URI = os.environ.get(
    "MONGO_URI",
    "mongodb+srv://harshavvc234:wP5Ifcv0FwJuj3vG@cluster444.x7wmqzg.mongodb.net/"
)
client = MongoClient(MONGO_URI)

db = client["todo_database"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "Missing fields"}), 400

    todo = {
        "name": item_name,
        "description": item_description
    }

    collection.insert_one(todo)
    return jsonify({"message": "To-Do item submitted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
