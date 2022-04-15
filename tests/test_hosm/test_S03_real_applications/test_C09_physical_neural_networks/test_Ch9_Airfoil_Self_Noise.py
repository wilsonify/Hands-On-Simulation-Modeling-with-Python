import os.path

import pandas as pd
import pytest

from hosm.S03_real_applications.C09_physical_neural_networks.Ch9_Airfoil_Self_Noise import (
    read_ASNData,
    split_data,
    asn,
    linear_fit,
    linear_predict,
    mlp_fit,
    mlp_predict
)

path_to_here = os.path.abspath(os.path.dirname(__file__))


def test_smoke():
    print("fire?")


@pytest.fixture(name="ASNData")
def test_read_ASNData():
    ASNData = read_ASNData(f"{path_to_here}/airfoil_self_noise.dat")
    return ASNData


def test_asn(ASNData):
    asn(ASNData)


def test_split_data(ASNData):
    X_train, X_test, Y_train, Y_test = split_data(ASNData)
    assert X_train.shape == (1052, 5)
    assert X_test.shape == (451, 5)
    assert Y_train.shape == (1052,)
    assert Y_test.shape == (451,)


def test_linear_fit(ASNData):
    X_train, X_test, Y_train, Y_test = split_data(ASNData)
    lr = linear_fit(X_train, Y_train)
    Y_predLM = linear_predict(lr, X_test)


def test_mlp_fit(ASNData):
    X_train, X_test, Y_train, Y_test = split_data(ASNData)
    mlp = mlp_fit(X_train, Y_train)
    Y_predMLPReg = mlp_predict(mlp, X_test)
