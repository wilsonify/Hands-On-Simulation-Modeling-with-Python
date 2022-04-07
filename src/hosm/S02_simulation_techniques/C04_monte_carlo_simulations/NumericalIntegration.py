"""
Performing numerical integration using Monte Carlo
Monte Carlo simulations represent a numerical solution for calculating integrals.
In fact, with the use of the Monte Carlo algorithm,
it is possible to adopt a numerical procedure for the solution of mathematical problems,
with many variables that do not present an analytical solution.

The efficiency of the numerical solution increases compared to other methods when the size of the problem increases.

Let's analyze the problem of a definite integral.
In the simplest cases,
there are methods for integration that foresee the use of techniques such as integration by parts,
integration by replacement, and so on.
In more complex situations, however,
it is necessary to adopt numerical procedures that involve the use of a computer.
In these cases,
the Monte Carlo simulation provides a simple solution that's particularly useful in cases of multidimensional integrals.

However, it is important to highlight that the result that's returned by this simulation
approximates the integral and not its precise value.

Defining the problem In the following equation,
we denote with I the definite integral of the function f in the limited interval [a, b]:

𝐼 = ∫ from a to b 𝐹(𝑥) 𝑑x

In the interval [a, b], we identify the maximum of the function f and indicate it with U.

To evaluate the approximation that we are introducing,
we draw a base rectangle, [a, b], and the height, U.

The area under the function f(x), which represents the integral of f(x),
will surely be smaller than the area of the base rectangle, [a, b], and the height, U.

The following diagram shows the area subtended by the function f —
which represents the integral of f(x) —
and the area A of the rectangle with base [a, b] and height U,
which represents our approximation:Performing numerical integration using Monte Carlo

we can identify the following intervals:
• x ∈ [a, b]
• y ∈ [0, U]

In the Monte Carlo simulation, x and y both represent random numbers.
At this point, we can consider a point in the plane of the Cartesian coordinates, (x, y).
Our goal is to determine the probability that this point is within the area under the curve;
that is, that it is y ≤ f(x).
We can identify two areas:
• The area subtended by the function f, which coincides with the definite integral I
• The area A of the rectangle with base [a, b] and height U

Let's try to write a relationship between the probability and these two areas:
𝑃(𝑦 ≤ 𝑓(𝑥)) = 𝐼/A = I/ ((𝑏𝑏 − 𝑎𝑎) ∗ 𝑈)

It is possible to estimate the probability, P (y <= f (x)), through Monte Carlo simulation.
In fact, in Applying the Monte Carlo method for Pi estimation section, we faced a similar case.
To do this, N pairs of random numbers (x i , y i ) are generated, as follows:
x_𝑖 ∈ [a, b]
y_𝑖 ∈ [0, U]

Generating random numbers in the intervals considered will certainly determine conditions in which y i ≤ f (x i ) will result. If we number this quantity and denote it with
the symbol M, we can analyze its variation. This is an approximation whose accuracy
increases as the number of random number pairs (x i , y i ) generated increases. The
approximation of the calculation of the probability P(y < f(x)) will therefore be equal to
the following value:
𝜇 = 𝑀/𝑁

After calculating this probability, it will be possible to trace the value of the integral using
the previous equation, as follows:

𝐼 ≅ 𝜇 ∗ (𝑏 − 𝑎) ∗ 𝑈 = M/N ∗ (𝑏 − 𝑎) ∗ 𝑈 = M/N ∗ 𝐴

This is the mathematical representation of the problem.
Now, let's see the numerical solution.

We will begin by setting up the components that we will need for the simulation,
starting from the libraries that we will use to defining the function and its domain of existence.
The Python code for numerical integration through the Monte Carlo method is shown here:
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def plot_area(f, a, b, XLin, YLin, XIntegral, YIntegral, XRectangle, YRectangle):
    plt.axis([0, b, 0, f(b)])
    plt.plot(XLin, YLin, color="red", linewidth="4")
    plt.scatter(XIntegral, YIntegral, color="blue", marker=".")
    plt.scatter(XRectangle, YRectangle, color="yellow", marker=".")
    plt.title("Numerical Integration using Monte Carlo method")
    plt.show()


def numerical_integration(f, a, b):
    random.seed(2)
    NumSteps = 1000000
    XIntegral = []
    YIntegral = []
    XRectangle = []
    YRectangle = []

    ymin = f(a)
    ymax = ymin
    for i in range(NumSteps):
        x = a + (b - a) * float(i) / NumSteps
        y = f(x)
        if y < ymin: ymin = y
        if y > ymax: ymax = y

    A = (b - a) * (ymax - ymin)
    N = 1000000
    M = 0
    for k in range(N):
        x = a + (b - a) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        if y <= f(x):
            M += 1
            XIntegral.append(x)
            YIntegral.append(y)
        else:
            XRectangle.append(x)
            YRectangle.append(y)
    NumericalIntegral = M / N * A

    XLin = np.linspace(a, b)
    YLin = []
    for x in XLin:
        YLin.append(f(x))

    return NumericalIntegral


if __name__ == "__main__":
    f = lambda x: x ** 2
    a = 0.0
    b = 3.0
    ni = numerical_integration(f, a, b)
    print(f"Numerical integration = {ni}")
