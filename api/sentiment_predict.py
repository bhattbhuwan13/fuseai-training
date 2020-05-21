from __future__ import absolute_import
import os
import sys
import argparse
import time
import json
print(os.path.realpath(__file__))

full_absolute_location = os.path.realpath(__file__) 
full_absolute_location = full_absolute_location.split("/")
full_absolute_location = "/".join( full_absolute_location[:-2])
sys.path.append(os.path.join(full_absolute_location, 'src'))


from models.predict_model import make_predictions

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
from flask import jsonify

from bson.json_util import dumps
from bson.json_util import loads

from pymongo import MongoClient

app = Flask(__name__, template_folder="./templates")
MONGO_URL = "mongodb://127.0.0.1:27017"

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_sentiment', methods=['GET', 'POST'])
def find_sentiment():
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        text = request.form['text']
        a = time.monotonic()
        sentiment, probability = make_predictions(text)
        sentiment = sentiment[0]
        b = time.monotonic()
        time_elapsed = b - a

        database_item = {
                    'query':text,
                    'sentiment':sentiment,
                    'eta' : time_elapsed,
                    'confidence': probability
                    }
        # inserting to dtabase
        client = MongoClient(MONGO_URL)
        db=client['sentiments']
        sentiments = db.sentiments
        sentiments.insert_one(database_item)

        return render_template('submit_text.html', message = sentiment)

    return render_template('submit_text.html')


@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        text = request.args.get("text", '')
        a = time.monotonic()
        print("printing the text {}".format(request.get_json(force=True)['text']))
        text = request.get_json(force=True)['text']
        sentiment, probability = make_predictions(text)
        sentiment = sentiment[0]
        b = time.monotonic()
        time_elapsed = b-a
        
        response = {
                    'sentiment':sentiment,
                    'eta' : time_elapsed,
                    'confidence': probability
                }
        response = jsonify(response)

        database_item = {
                    'query':text,
                    'sentiment':sentiment,
                    'eta' : time_elapsed,
                    'confidence': probability
                    }
        # inserting to dtabase
        client = MongoClient(MONGO_URL)
        db=client['sentiments']
        sentiments = db.sentiments
        sentiments.insert_one(database_item)
        return response


@app.route('/get_all_items', methods=['GET'])
def get_all_items():
    if request.method == 'GET':
        # Form being submitted; grab data from form.

        # getting all request from database
        client = MongoClient(MONGO_URL)
        db=client['sentiments']
        sentiments = db.sentiments
        
        items = []
        for item in sentiments.find():
            item.pop('_id')
            items.append(item)


        resp = jsonify(items)
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
