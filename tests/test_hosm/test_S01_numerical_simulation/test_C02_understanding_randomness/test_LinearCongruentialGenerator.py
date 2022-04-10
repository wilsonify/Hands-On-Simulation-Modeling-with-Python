import numpy as np
from hosm.S01_numerical_simulation.C02_understanding_randomness.LinearCongruentialGenerator import (
    LCG,
)


def test_smoke():
    print("fire?")


def test_lcg():
    result = []
    generator = LCG()
    for _ in range(1, 17):
        result += [round(next(generator), 2)]
    assert result == [0, 4, 2, 3, 0, 4, 2, 3, 0, 4, 2, 3, 0, 4, 2, 3]
