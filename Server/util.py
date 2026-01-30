import pickle
import json
import os
import numpy as np

__locations = None
__data_columns = None
__model = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __data_columns
    global __locations
    global __model

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")

    with open(os.path.join(ARTIFACTS_DIR, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    if __model is None:
        with open(os.path.join(ARTIFACTS_DIR, "banglore_home_prices_model.pickle"), "rb") as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")
    print("Locations loaded:", len(__locations))


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

load_saved_artifacts()
