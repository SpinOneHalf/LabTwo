from flask import Flask
app = Flask(__name__)
from time import time

@app.route('/')
def hello_world():
    return 'Hello world!'
@app.route("/time")
def time():
    return time()

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
