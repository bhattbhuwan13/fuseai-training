import numpy as np
import pandas as pd
import pickle
import sys
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn import preprocessing

def get_features(file_location):
    raw_data = pd.read_csv(file_location)
    raw_data.columns = ['index', 'sentiment', 'text']
    raw_data.set_index('index')

    raw_data['text'] = raw_data['text'].apply( lambda x: x.lower())


    path_to_base_folder = os.sys.path[0]
    path_to_base_folder = path_to_base_folder.split("/")
    path_to_base_folder = ("/").join(path_to_base_folder[:-2])
    print("path to base folder is {}".format(path_to_base_folder))
    # Reading the pickle files
    vectorizer_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/vectorizer.pkl', 'rb')
    label_encoder_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/label_encoder.pkl', 'rb')
    tf_idf_transformer_file = open(path_to_base_folder + '/models/encoder_and_vectorizer/tf_idf_transformer.pkl', 'rb')

    vectorizer = pickle.load(vectorizer_file)
    label_encoder = pickle.load(label_encoder_file)
    tf_idf_transformer = pickle.load(tf_idf_transformer_file)
    
    # Closing the files
    vectorizer_file.close()
    label_encoder_file.close()
    tf_idf_transformer_file.close()


    features = vectorizer.transform(
        raw_data['text']
    )

    features = tf_idf_transformer.transform(features)
    
    features_nd = features.toarray()
    
    raw_data['sentiment_encoded'] = label_encoder.transform(raw_data['sentiment'])

    X, y = features_nd, raw_data['sentiment_encoded']

    return(X, y)


def main():
    file_location = sys.argv[1]
    X_dummy, y_dummy = get_features(file_location)
    print(X_dummy[:4], y_dummy[:4])



if __name__ == "__main__":
    main()
