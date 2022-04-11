import random

import numpy as np


def test_smoke():
    print("fire?")


def test_bd():
    random.seed(1)
    P1 = np.random.binomial(n=10, p=0.5, size=1000)
    assert P1.shape == (1000,)
