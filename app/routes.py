from flask import Blueprint, jsonify
import json
import os

main = Blueprint('main', __name__)

@main.route('/api/distributors', methods=['GET'])
def get_distributors():
    data_file = os.path.join(os.path.dirname(__file__), 'data', 'power_distributors.json')
    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)