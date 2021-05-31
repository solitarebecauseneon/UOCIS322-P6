# Streaming Service

from flask import Flask, request
import os
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevetdb


def retrieve():
    """
    retrieves all data from database
    """
    app.logger.debug("Pulling data from db")
    temp = db.timestable.find()
    result = []
    for i in temp:
        del i['_id']
        result.append(i)
    app.logger.debug("MangoDB documents: {}".format(result))
    return result


def csv_form(result):
    return None


def json_form(result):
    return None


class ListAll(Resource):
    def get(self, dtype='json'):
        request.args.get('top', default=-1)
        if dtype == 'csv':
            return csv_form(retrieve())
        return json_form(retrieve())


class ListOpenOnly(Resource):
    def get(self, dtype='json'):
        request.args.get('top', default=-1)
        if dtype == 'csv':
            return csv_form(retrieve())
        return json_form(retrieve())


class ListCloseOnly(Resource):
    def get(self, dtype):
        request.args.get('top', default=-1)
        if dtype == 'csv':
            return csv_form(retrieve())
        return json_form(retrieve())


# Create routes
# Another way, without decorators
DEFAULT_URL = "http://" + os.environ['BACKEND_ADDR'] + os.environ['BACKEND_PORT']
api.add_resource(ListAll, (DEFAULT_URL + '/listAll/<str:dtype>'))
api.add_resource(ListOpenOnly, (DEFAULT_URL + '/listOpenOnly/<str:dtype>'))
api.add_resource(ListCloseOnly, (DEFAULT_URL + '/listCloseOnly/<str:dtype>'))


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
