from flask import Flask, jsonify, redirect
from flask import request
from flask_session import Session # Server side application session
import redis

# generator.py to generate new link
import generator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"


