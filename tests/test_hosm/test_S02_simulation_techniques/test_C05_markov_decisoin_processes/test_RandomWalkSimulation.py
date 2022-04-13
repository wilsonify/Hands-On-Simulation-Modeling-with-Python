from random import seed
from random import random
from matplotlib import pyplot

from hosm.S02_simulation_techniques.C05_markov_decision_processes.RandomWalkSimulation import rw


def test_smoke():
    print("fire?")


def test_rws():
    walk = rw()
    assert len(walk) == 1000
