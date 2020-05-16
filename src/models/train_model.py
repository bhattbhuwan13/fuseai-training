from __future__ import absolute_import
import sys
import os
import argparse

full_absolute_location = os.sys.path[0]
full_absolute_location = full_absolute_location.split("/")
full_absolute_location = "/".join( full_absolute_location[:-1])
sys.path.append(os.path.join(full_absolute_location, 'features'))

import numpy as np
import pandas as pd
import pickle

from datetime import datetime, date
from build_features import get_features
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier


def save_model(model, location='../../models/', name='SGD'):
    current_date = str(date.today())
    current_time = datetime.today().strftime("%H:%M:%S")

    complete_location = location + name + '_' + current_date + '_' + current_time + '.pkl'
    try:
        with open(complete_location, 'wb') as file:
            pickle.dump(model, file)
        print("Model {} successfully saved at {}".format(model, location))

    except:
        print("Model saving failed")


def train_model(dataset_location):
    RANDOM_STATE = 42
    X, y = get_features(dataset_location)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y)
    classifier = SGDClassifier(random_state=RANDOM_STATE)
    classifier.fit(X_train, y_train)

    y_train_pred = classifier.predict(X_train)
    train_accuracy = accuracy_score(y_train, y_train_pred)
    print("The accuracy of training set is {}%".format(train_accuracy* 100))

    y_test_pred = classifier.predict(X_test)
    prediction_accuracy = accuracy_score(y_test_pred, y_test)
    print("The accuracy of prediction set is {}%".format(prediction_accuracy* 100))

    return classifier


def main():
    RANDOM_STATE = 42


    dataset_and_model_location = os.sys.path[0]
    print("dataset and moedel location = {}".format(dataset_and_model_location))
    dataset_and_model_location = dataset_and_model_location.split("/")
    dataset_and_model_location = "/".join(dataset_and_model_location[:-2])
    print("dataset and moedel location = {}".format(dataset_and_model_location))

    FILE_LOCATION = dataset_and_model_location + '/data/raw/ISEAR.csv'
    MODEL_LOCATION = dataset_and_model_location + '/models/'

    NAME = 'SGD'
   
    print(FILE_LOCATION, MODEL_LOCATION)
    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Add long and short argument
    parser.add_argument("--model_location", "-m", help="Location to store the saved model")
    parser.add_argument('--dataset_location', '-d', help="Location to store the dataset")

    # Read arguments from the command line
    args = parser.parse_args()

    if args.model_location:
        MODEL_LOCATION = os.path.abspath(args.model_location) 
        print("model will be stored at {}".format(MODEL_LOCATION))
    else:
        MODEL_LOCATION = os.path.abspath(MODEL_LOCATION) 
        print("Explicit model location not supplied, model will be stored at defaut location - {}".format(MODEL_LOCATION))

    if args.dataset_location:
        FILE_LOCATION = os.path.abspath(args.dataset_location) 
        print("Dataset will be stored at {}".format(FILE_LOCATION))
    else:
        FILE_LOCATION = os.path.abspath(FILE_LOCATION) 
        print("Explicit dataset path not supplied, reading dataset from the default location - {}".format(FILE_LOCATION))



    model = train_model(FILE_LOCATION)
    save_model(model, MODEL_LOCATION, NAME)

if __name__ == "__main__":
    main()
