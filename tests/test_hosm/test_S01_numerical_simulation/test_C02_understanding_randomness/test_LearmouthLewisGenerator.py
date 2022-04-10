from inspect import getmembers, isfunction

from hosm.S01_numerical_simulation.C02_understanding_randomness import LearmouthLewisGenerator
from hosm.S01_numerical_simulation.C02_understanding_randomness.LearmouthLewisGenerator import LLG


def test_smoke():
    print("fire?")
    print(getmembers(LearmouthLewisGenerator, isfunction))


def test_llg():
    result = []
    generator = LLG()
    for i in range(1, 10):
        result += [round(next(generator), 4)]
    assert result == [0.0, 0.0, 0.0, 0.0015, 0.1105, 0.2878, 0.5828, 0.7089, 0.1686]
