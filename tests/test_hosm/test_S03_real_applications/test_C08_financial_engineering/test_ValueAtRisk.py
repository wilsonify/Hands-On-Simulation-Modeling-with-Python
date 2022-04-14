import datetime as dt
import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import pytest
from scipy.stats import norm

from hosm.S03_real_applications.C08_financial_engineering.ValueAtRisk import read_StockClose, value_at_risk


def test_smoke():
    print("fire?")


@pytest.fixture(name="stock_close")
def test_read_StockClose():
    stock_close = read_StockClose()
    return stock_close


def test_value_at_risk(stock_close):
    value_at_risk(stock_close)
