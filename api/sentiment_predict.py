from __future__ import absolute_import
import os
import sys
import argparse
import time
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

app = Flask(__name__, template_folder="./templates")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_sentiment', methods=['GET', 'POST'])
def find_sentiment():
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        text = request.form['text']
        print(text)
        sentiment = make_predictions(text)
        print(sentiment)
        return render_template('submit_text.html', message = sentiment[0])

    return render_template('submit_text.html')


@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        text = request.args.get("text", '')
        a = time.monotonic()
        print("printing the text {}".format(request.get_json(force=True)['text']))
        text = request.get_json(force=True)['text']
        sentiment = make_predictions(text)
        sentiment = sentiment[0]
        b = time.monotonic()
        time_elapsed = b-a
        
        response = {
                    'sentiment':sentiment,
                    'eta' : time_elapsed
                }
        response = jsonify(response)
        return response


if __name__ == '__main__':
    app.run()
