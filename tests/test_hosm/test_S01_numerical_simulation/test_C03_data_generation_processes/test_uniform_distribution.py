import numpy as np


def test_smoke():
    print("fire?")


def test_ud():
    result = np.random.uniform(low=1, high=100, size=100)
    assert result.shape == (100,)


def test_ud2():
    result = np.random.uniform(low=1, high=100, size=10000)
    assert result.shape == (10000,)
