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
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import Form
from wtforms import TextField
from flask import jsonify

app = Flask(__name__, template_folder="./templates")


# Setting for database

app.config['DEBUG'] = True
POSTGRES = {
    'user': 'fuseai',
    'pw': 'fuseai',
    'db': 'text_sentiment',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class PredictionsModel(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.String())
    prediction = db.Column(db.String())
    time = db.Column(db.Float())

    def __init__(self, name, model, doors):
        self.input_text = input_text
        self.prediction = prediction
        self.time = time

    def __repr__(self):
        return f"<Prediction {self.input_text} -> {self.prediction}>"



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
        a = time.monotonic()
        # Form being submitted; grab data from form.
        text = request.args.get('text', '')
        sentiment = make_predictions(text)
        sentiment = sentiment[0]

        b = time.monotonic()
        c = b-a

        # For saving to database
        new_prediction = PredictionsModel(input_text = text, prediction = sentiment, time = c)
        db.session.add(new_prediction)
        db.session.commit()
        # Database task finished

        response = {
                    'text' : text,
                    'sentiment': sentiment,
                    'messsage' : "New entry saved to database"
                }
        response = jsonify(response)
        return response



if __name__ == '__main__':
    app.run()
