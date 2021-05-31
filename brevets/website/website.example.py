from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

URL_TRACE = "http://" + os.environ['BACKEND_ADDR'] + os.environ['BACKEND_PORT']

@app.route('/')
@app.route('/index')
def home():
    render_template('index.html')


@app.route('/listeverything')
def listeverything():
    r = requests.get('http://restapi:5000/listAll')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
