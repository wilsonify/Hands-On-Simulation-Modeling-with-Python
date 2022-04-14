import pandas as pd
import random
import numpy as np

from hosm.S03_real_applications.C10_project_management.MonteCarloTasksScheduling import mcts


def test_smoke():
    print("fire?")


def test_mcts():
    data = mcts()
    assert data.shape == (10000, 6)
