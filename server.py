import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@ app.route('/')
def hello_world():
    return 'Hello World from Flask!'


port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0', port=port)
