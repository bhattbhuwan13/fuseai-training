from __future__ import absolute_import
import os
import sys
import argparse

print(os.path.realpath(__file__))

full_absolute_location = os.path.realpath(__file__) 
full_absolute_location = full_absolute_location.split("/")
full_absolute_location = "/".join( full_absolute_location[:-2])
sys.path.append(os.path.join(full_absolute_location, 'src'))


from models.predict_model import make_predictions

sentiment = make_predictions("I am very very happy")

print(sentiment)
