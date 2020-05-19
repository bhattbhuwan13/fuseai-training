from __future__ import absolute_import
import sys
import os
import joblib
import argparse

full_absolute_location = os.path.realpath(__file__) 
print("path from predict are {} ".format(os.path.realpath(__file__)))
full_absolute_location = full_absolute_location.split("/")
full_absolute_location = "/".join(full_absolute_location[:-2])
#sys.path.append(os.path.join(full_absolute_location, 'src'))
sys.path.append(full_absolute_location)


import numpy as np
import pandas as pd
import pickle

from datetime import datetime, date
from features.build_features import get_features
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.feature_extraction.text import TfidfVectorizer


def get_artifacts():
    path_to_base_folder = os.path.realpath(__file__) 
    path_to_base_folder = path_to_base_folder.split("/")
    path_to_base_folder = ("/").join(path_to_base_folder[:-3])
    print("path to base folder is {}".format(path_to_base_folder))

    # Reading the pickle files
    vectorizer_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/vectorizer.pkl', 'rb')
    label_encoder_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/label_encoder.pkl', 'rb')
    tf_idf_transformer_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/tf_idf_transformer.pkl', 'rb')
    model_file = open(path_to_base_folder + '/models/SGD_2020-05-15_17:00:01.pkl', 'rb')

    vectorizer = pickle.load(vectorizer_file)
    label_encoder = pickle.load(label_encoder_file)
    tf_idf_transformer = joblib.load(path_to_base_folder + '/models/tfidt_feature_vector.pkl')
    model = joblib.load(path_to_base_folder + '/models/Naive_bayes_model.pkl')
    
    # Closing the files
    vectorizer_file.close()
    label_encoder_file.close()
    #tf_idf_transformer_file.close()
    #model_file.close()

    return vectorizer, label_encoder, tf_idf_transformer, model


def make_predictions(text):
    text = text.lower()
    text_list = []
    text_list.append(text)
    text = text_list
    vectorizer, label_encoder, tf_idf_transformer, model = get_artifacts()

    #count_vec = CountVectorizer(vocabulary=vectorizer.vocabulary_, analyzer='word', stop_words='english', ngram_range=(2, 2))

    #features = tf_idf_transformer.transform(
    #
    #    text
    #)
    #tf_idf_transformer = TfidfTransformer()
    features = tf_idf_transformer.transform(text_list)
    
    features_nd = features #features.toarray()
    #print(features_nd)
    #features_nd = features_nd[0]
    #print(sum(features_nd))
    #features_nd = features_nd.reshape(-1, 1).T
    result = model.predict(features_nd)
    print("The probability is : {}".format(model.predict_proba(features_nd)))
    prob = max(model.predict_proba(features_nd)[0])
    print(prob)

    #result = label_encoder.inverse_transform(result)
    return result, prob


def main():
    sentiment = make_predictions("I hate you. You are the worst person")
    print(sentiment)

if __name__ == '__main__':
    main()
