from flask import Flask
from redis import Redis, RedisError
import os
import socket

# connect to Redis
redis = Redis(host='redis', db=0, socket_connect_timeout=2, socket_timeout=2)

# define flask app
app = Flask(__name__)

# entrypoint
@app.route('/')
def index():
    try:
        visits = redis.incr('visit_counter')
    except RedisError as e:
        visits = '<i>Cannot connect to Redis, counter disabled</i>'

    html = '<h3>Hello {name}!</h3>' \
           '<b>Hostname:</br> {hostname}<br/>' \
           '<b>Visits:</br> {visits}'

    return html.format(
        name=os.getenv('NAME', 'World'),
        hostname=socket.gethostname(),
        visits=visits,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
