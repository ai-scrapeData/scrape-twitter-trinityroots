from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://adminuser:admin1234@ds227199.mlab.com:27199/gcp-database?retryWrites=false'

mongo = PyMongo(app)
api = Api(app)
parser = reqparse.RequestParser()

parser.add_argument('time_year', type=str)
parser.add_argument('time_month', type=str)
parser.add_argument('time_day', type=str)
parser.add_argument('word_feel', type=str)
# https://scrape-selenium-pantip.herokuapp.com/
class AllData(Resource):
    def get(self):
        try:
            query = {}
            projection = {'_id':False}
            scoreSportData = mongo.db.comment.find(query, projection).sort([("api.author_time_stamp", -1)])
            # .limit(10)
            listData = []
            for element in scoreSportData:
                listData.append(element)
            return jsonify(listData)
        except:
            return 'Not found'
class DateTime(Resource):
    def get(self):
        args = parser.parse_args()
        year = args['time_year']
        month = args['time_month']
        day = args['time_day']
        query = {}
        if year and month and day: 
            query = {
                "api.time_year": {"$eq": year},
                "api.time_month": {"$eq": month},
                "api.time_day": {"$eq": day}
            }
            # http://127.0.0.1:5000/datetime?year=2018&month=10&day=16
            # http://127.0.0.1:5000/datetime?day=16&month=10&year=2018
        elif year and month:
            query = {
                "api.time_year": {"$eq": year},
                "api.time_month": {"$eq": month}
            }
            # http://127.0.0.1:5000/datetime?year=2018&month=10
            # http://127.0.0.1:5000/datetime?month=10&year=2018
        elif month and day:
            query = {
                "api.time_month": {"$eq": month},
                "api.time_day": {"$eq": day}
            }
            # http://127.0.0.1:5000/datetime?month=10&day=16
            # http://127.0.0.1:5000/datetime?day=16&month=10
        elif year:
            query = {
                "api.time_year": {"$eq": year}
            }
            # http://127.0.0.1:5000/datetime?year=2018
        elif month:
            query = {
                "api.time_month": {"$eq": month}
            }
            # http://127.0.0.1:5000/datetime?month=10
        elif day:
            query = {
               "api.time_day": {"$eq": day} 
            }
            # http://127.0.0.1:5000/datetime?day=10

        projection = {'_id':False}
        print(query)
        date_time_category = mongo.db.comment.find(query, projection).sort([("api.author_time_stamp", -1)]).limit(10)
        return jsonify(list(date_time_category))

class WordSensitive(Resource):
    def get(self):
        args = parser.parse_args()
        word_feel = args['word_feel']
        query = {}
        if word_feel:
            query = {
                "api.word_feel": {"$eq": word_feel} 
            }
        projection = {'_id':False}
        print(query)
        date_time_category = mongo.db.comment.find(query, projection).sort([("api.author_time_stamp", -1)]).limit(10)
        return jsonify(list(date_time_category))

api.add_resource(AllData, '/')
api.add_resource(DateTime, '/datetime')
api.add_resource(WordSensitive, '/word')





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
