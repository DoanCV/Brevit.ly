from flask import Flask, redirect
from flask import request
from flask_session import Session # Server side application session
import redis

# generator.py to generate new link
import generator

# startup FLask app
app = Flask(__name__)

# startup NoSQL DB (default db is 0 but lets make it explicit)
redis_session = redis.Redis(host = "localhost", port = 6379, db = 0)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)


@app.route('/', methods = ['POST'])
def index():
     
    long_url = request.form['URI']

    URI = generator.generator(long_url)

    redis_session.set(URI, long_url)

    return "http://localhost:5000/" + URI


@app.route('/<short_url>')
def redirect(short_url):
    
    URI = redis_session.get(short_url)

    # If there is a valid url, turn unicode to ASCII, then send redirect response
    if URI:
        URI = URI.decode("UTF-8")
    
    if URI:
        return redirect(URI, code = 302)
    else:
        return '"Error" : "No url available"'


@app.route('/shorten', methods = ['POST'])
def reindex():
    """
    If the generator fails we enter this route to create attempt another url creation
    """
    long_url = request.headers.get('URI')

    URI = generator.generator(long_url)

    redis_session.set(URI, long_url)

    return "http://localhost:5000/" + URI


if __name__ == '__main__':
    app.run()