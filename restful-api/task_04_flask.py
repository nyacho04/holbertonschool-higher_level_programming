#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        abort(400, description="Request data is missing")
    if 'username' not in data:
        abort(400, description="Username is required")

    username = data['username']
    if username in users:
        abort(400, description="Username already exists")

    users[username] = {
        "name": data.get("name", "Unknown"),
        "age": data.get("age", 0),
        "city": data.get("city", "Unknown")
    }
    return jsonify({"message": generate_message("User added"), "user": users[username]}), 201

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

def generate_message(message):
    return message

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)