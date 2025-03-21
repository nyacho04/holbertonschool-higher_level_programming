#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

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
        return jsonify({"error": "Request data is missing"}), 400
    
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    user_data = {
        "username": username,
        "name": data.get("name", "Unknown"),
        "age": data.get("age", 0),
        "city": data.get("city", "Unknown")
    }
    users[username] = user_data
    
    return jsonify({"message": "User added", "user": user_data}), 201

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)