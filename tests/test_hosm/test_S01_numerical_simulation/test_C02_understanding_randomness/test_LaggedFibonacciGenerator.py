from hosm.S01_numerical_simulation.C02_understanding_randomness.LaggedFibonacciGenerator import LFG


def test_smoke():
    print("fire?")


def test_LFG():
    result = []
    generator = LFG()
    for i in range(101):
        result += [next(generator)]
