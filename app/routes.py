from flask import jsonify
from app import app
import os
import json

@app.route('/api/data', methods=['GET'])
def get_data():
    json_path = os.path.join(app.root_path, 'data', 'power_distributors.json')
    with open(json_path, 'r') as file:
        data = json.load(file)
    return jsonify(data)