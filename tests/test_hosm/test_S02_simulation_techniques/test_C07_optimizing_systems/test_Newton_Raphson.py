import numpy as np
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C07_optimizing_systems.Newton_Raphson import nr


def test_smoke():
    print("fire?")


def test_nr():
    x = np.linspace(0, 3, 100)
    y = x ** 3 - 2 * x ** 2 - x + 2
    nr(x, y)
