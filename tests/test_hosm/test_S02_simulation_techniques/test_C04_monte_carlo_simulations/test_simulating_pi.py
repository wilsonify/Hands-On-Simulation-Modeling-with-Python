import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pytest

from hosm.S02_simulation_techniques.C04_monte_carlo_simulations.simulating_pi import estimate_pi


def test_smoke():
    print("fire?")


def test_spi():
    pi = estimate_pi()
    assert pi == pytest.approx(3.14, abs=0.1)
