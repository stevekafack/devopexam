
#section1.6
from flask import Flask, request
import logging
import statsd

app = Flask(__name__)

# Configure logging
# in year month day and timestamp
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Configure StatsD client
statsd_client = statsd.StatsClient(host='localhost', port=8125)

# Define a route
@app.route('/')
def index():
    try:
        # Perform some action that may raise an exception
        # For example, accessing an undefined variable
        result = 1 / 0
    except Exception as e:
        # Log the exception at the error level
        logging.error(str(e))
        # Increment the counter metric in StatsD
        statsd_client.incr('exceptions.count')

    return 'Hello, World this a new devop enviroment kafack!'

if __name__ == '__main__':
    app.run()
