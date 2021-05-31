from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

URL_TRACE = "http://" + os.environ['BACKEND_ADDR'] + ":" + os.environ['BACKEND_PORT']


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return render_template('404.html'), 404


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/listevery')
def listeverything():
    json_csv = request.args.get('json_csv')
    json_csv = str(json_csv)
    r = requests.get(URL_TRACE + '/listAll' + '/' + json_csv)
    app.logger.debug("r.text: {}".format(r.text))
    return r.text


@app.route('/listopen')
def listopenonly():
    json_csv = request.args.get('json_csv')
    json_csv = str(json_csv)
    r = requests.get(URL_TRACE + '/listOpenOnly' + '/' + json_csv)
    app.logger.debug("r.text: {}".format(r.text))
    return r.text


@app.route('/listclose')
def listcloseonly():
    json_csv = request.args.get('usr_args')
    json_csv = str(json_csv)
    r = requests.get(URL_TRACE + '/listCloseOnly' + '/' + json_csv)
    app.logger.debug("r.text: {}".format(r.text))
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
