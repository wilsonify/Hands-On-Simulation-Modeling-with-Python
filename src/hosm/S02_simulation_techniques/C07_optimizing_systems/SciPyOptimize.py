"""
Discovering the multivariate optimization methods in Python

In this section, we will analyze some numerical optimization methods contained in the Python SciPy library.

SciPy is a collection of mathematical algorithms and functions based on NumPy.

It contains a series of commands and high-level classes that can be used to manipulate and display data.

With SciPy, functionality is added to Python,
making it a data processing and system prototyping environment, similar to commercial systems such as MATLAB.

Scientific applications that use SciPy benefit from the development of
add-on modules in numerous fields of numerical computing made by developers around the world.

Numerical optimization problems are also covered among the available modules.
The SciPy optimize module contains numerous functions for the minimization maximization of objective functions,
both constrained and unconstrained.
It treats nonlinear problems with support for both local and global optimization algorithms.

In addition, problems regarding linear programming, constrained and nonlinear least squares,
search for roots, and the adaptation of curves are dealt with.
In the following sections, we will analyze some of them.


The Nelder–Mead method

Most of the well-known optimization algorithms are based on the concept of derivatives
 and on the information that can be deduced from the gradient.

However,
many optimization problems deriving from real applications are
characterized by the fact that the analytical expression of the objective function is not known,
which makes it impossible to calculate its derivatives,
or because is particularly complex,
so coding the derivatives may take too long.

To solve this type of problem,
several algorithms have been developed that do not attempt to approximate the gradient but rather use the values of
the function in a set of sampling points to determine a new iteration by other means.

The Nelder-Mead method tries to minimize a nonlinear function by
evaluating test points that constitute a geometric form called a simplex.

Important Note
A simplex is defined as a set of closed and convex points of a Euclidean space
that allow us to find the solution to the typical optimization problem of linear programming.

Using Simulation to Improve and Optimize Systems
The choice of geometric figure for the simplex is mainly due to two reasons:
the ability of the simplex to adapt its shape to the trend in the space of the objective function deforming itself,
and the fact that it requires the memorization of only n + 1 points.

Each iteration of a direct search method based on the simplex begins with a simplex,
specified by its n + 1 vertices and the values of the associated functions.

One or more test points and the respective values of the function are calculated,
and the iteration ends with a new simplex so that the values of the function
in its vertices satisfy some form of descent condition with respect to the previous simplex.

The Nelder-Mead algorithm is particularly sparing in terms of its evaluation of the function at each iteration,
given that, in practice, it typically requires only one or two evaluations of the function to build a new simplex.

However, since it does not use any gradient assessment,
it may take longer to find the minimum.

This method is easily implemented in Python using the minimize routine of the SciPy optimize module.
Let's look at a simple example of using this method:

"""
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def matyas(x):
    return 0.26 * (x[0] ** 2 + x[1] ** 2) - 0.48 * x[0] * x[1]


def booth(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


def plot_matyas(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.RdBu, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.show()


def nm(f):
    x0 = np.array([-10, 10])
    NelderMeadOptimizeResults = minimize(f, x0, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})
    print(NelderMeadOptimizeResults.x)


def po(f):
    x0 = np.array([-10, 10])
    PowellOptimizeResults = minimize(f, x0, method='Powell', options={'xtol': 1e-8, 'disp': True})
    print(PowellOptimizeResults.x)


if __name__ == "__main__":
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z = matyas([x, y])
    plot_matyas(x, y, z)
    nm(matyas)
    po(matyas)
