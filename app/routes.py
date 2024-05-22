from flask import jsonify
from app import app

@app.route('/api/data', methods=['GET'])
def get_data():
    with open('app/data/power_distributors.json', 'r') as file:
        data = file.read()
    return jsonify(data)