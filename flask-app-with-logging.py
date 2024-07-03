import os
import logging
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info(f"Received request from {request.remote_addr}")
    return "Hello, World!"

@app.route('/error')
def error():
    logger.error("This is a sample error")
    return "Error logged", 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)