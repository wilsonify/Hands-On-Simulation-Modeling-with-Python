import random
import numpy as np
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C06_resampling.BootstrapEstimator import bootstrap


def test_smoke():
    print("fire?")


def test_bse():
    psm = bootstrap()
    assert len(psm) == 10000
