import numpy as np
import matplotlib.pyplot as plt

from hosm.S03_real_applications.C08_financial_engineering.StandardBrownianMotion import sbm


def test_smoke():
    print("fire?")


def test_sbm():
    sb = sbm()
    assert len(sb) == 1000
