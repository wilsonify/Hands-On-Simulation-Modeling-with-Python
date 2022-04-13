import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

from hosm.S02_simulation_techniques.C07_optimizing_systems.SciPyOptimize import matyas, nm, po


def test_smoke():
    print("fire?")


def tests_matyas():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z = matyas([x, y])


def test_nm():
    nm(matyas)


def test_po():
    po(matyas)
