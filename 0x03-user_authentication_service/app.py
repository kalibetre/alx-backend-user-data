#!/usr/bin/env python3
"""
Flask App
"""
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def getMessage() -> str:
    """ GET /
    Return:
      - {"message": "Bienvenue"}
    """
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """ POST /users
    Return:
        - registered user emails
    """
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email=email, password=password)
        return jsonify(email=user.email, message='user created'), 200
    except ValueError:
        return jsonify(message='email already registered'), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
