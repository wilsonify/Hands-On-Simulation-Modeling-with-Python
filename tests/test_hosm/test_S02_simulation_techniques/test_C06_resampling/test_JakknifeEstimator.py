import random
import statistics
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C06_resampling.JakknifeEstimator import jackknife_cv


def test_smoke():
    print("fire?")


def test_jackknife_cv():
    pv = jackknife_cv()
    assert len(pv) == 100
