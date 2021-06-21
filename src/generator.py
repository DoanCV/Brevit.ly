import random
import string

# instantiating in the function below is fine according to docs
import redis

def generator(data):
    """
    Get a short URI
    Keep generating 5 character short URL until it has not been used
    """

    redis_session = redis.Redis(host = 'localhost', port = 5000, db = 0)

    while True:
        
        URI = ""

        for i in range(0,5):

            URI += random.choice(string.ascii_letters)

        if not redis_session.get():
            return URI