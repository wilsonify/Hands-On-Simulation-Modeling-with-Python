import os.path
import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters
from hosm.S03_real_applications.C08_financial_engineering.AmazonStockMontecarloSimulation import (
    read_amzn_from_csv,
    LogReturns,
    amazon_trend,
    sim_stockprice

)

path_to_here = os.path.abspath(os.path.dirname(__file__))


def test_smoke():
    print("fire?")


@pytest.fixture(name="AmznData")
def test_read_amzn_from_csv():
    AmznData = read_amzn_from_csv(f"{path_to_here}/AMZN.csv")
    return AmznData


def test_LogReturns(AmznData):
    AmznLogReturns = LogReturns(AmznData)
    assert AmznLogReturns.shape == (2518, 1)


def test_amazon_trend(AmznData):
    amzn_trend = amazon_trend(AmznData)
    assert amzn_trend.shape == (2518, 1)


def test_sim_stockprice(AmznData):
    sp = sim_stockprice(AmznData)
    assert sp.shape == (2518, 20)
