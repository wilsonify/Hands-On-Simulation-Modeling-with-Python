import os.path

import matplotlib.pyplot as plt
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

from hosm.S03_real_applications.C09_physical_neural_networks.Ch9_Airfoil_Self_Noise import read_ASNData, split_data
from hosm.S03_real_applications.C09_physical_neural_networks.Ch9_Keras_Regression import keras_fit, keras_predict

path_to_here = os.path.abspath(os.path.dirname(__file__))


def test_smoke():
    print("fire?")


def test_kr():
    ASNData = read_ASNData()
    X_train, X_test, Y_train, Y_test = split_data(ASNData[:100])
    km = keras_fit(X_train, Y_train)
    Y_predKM = keras_predict(km, X_test)
    assert Y_predKM.shape == (30, 1)
