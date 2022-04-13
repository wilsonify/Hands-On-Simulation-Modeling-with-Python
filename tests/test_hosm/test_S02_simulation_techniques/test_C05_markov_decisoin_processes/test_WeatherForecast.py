import numpy as np
import matplotlib.pyplot as plt

from hosm.S02_simulation_techniques.C05_markov_decision_processes.WeatherForecast import weather


def test_smoke():
    print("fire?")


def test_wf():
    forecast = weather()
    assert len(forecast) == 364
