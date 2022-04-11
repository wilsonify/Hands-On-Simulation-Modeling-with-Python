from hosm.S01_numerical_simulation.C02_understanding_randomness.UniformityTest import LFG2


def test_smoke():
    print("fire?")


def test_ut():
    counts, Ypos, V = LFG2()
    assert counts.tolist() == [8, 3, 4, 7, 4, 5, 2, 3, 7, 7, 5, 4, 5, 2, 7, 5, 5, 5, 3, 9]
    assert Ypos.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert V == 14.8
