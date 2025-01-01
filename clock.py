from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world"

app.run(host='0.0.0.0', port=3000)