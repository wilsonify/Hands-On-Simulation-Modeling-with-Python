import random
import numpy as np
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C04_monte_carlo_simulations.NumericalIntegration import numerical_integration


def test_smoke():
    print("fire?")


def test_ni():
    f = lambda x: x ** 2
    a = 0.0
    b = 3.0
    ni = numerical_integration(f, a, b)
    assert round(ni, 2) == 9.0
