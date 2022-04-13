import numpy as np
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C07_optimizing_systems.GradientDescent import grad_desc


def test_smoke():
    print("fire?")

def test_gd():
    x = np.linspace(-1, 3, 100)
    y = x ** 2 - 2 * x + 1
    grad_desc(x, y)
