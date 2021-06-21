from flask import Flask, jsonify, redirect
from flask import request
from flask_session import Session # Server side application session
import redis

# generator.py to generate new link
import generator

# startup FLask app
app = Flask(__name__)

# startup NoSQL DB
redis_session = redis.Redis(host = "localhost", port = 5000, db = 0)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def hello_world():
    return "Hello world!"

if __name__ == '__main__':
    app.run()

