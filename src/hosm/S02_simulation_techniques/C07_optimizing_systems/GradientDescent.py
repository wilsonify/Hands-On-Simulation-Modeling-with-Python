"""
Explaining the trial and error method

The term trial and error defines a heuristic method that aims to
find a solution to a problem by attempting it and checking if it has produced the desired effect.
If so, the attempt constitutes a solution to the problem;
otherwise, we continue with a different attempt.

Let's analyze the essential characteristics of the method:

• It is oriented toward the solution:
It does not aim to find out why an attempt works, but simply seeks it.
• It is specific to the problem in question:
It has no claim to generalize to other problems.
• It is not optimal:
It usually limits itself to finding a single solution that will usually not be the best possible one.
• It does not require having thorough knowledge of it:
It proposes to find a solution to a problem of which little or nothing is known about it.

The trial and error method can be used to find all the solutions
to the problem or the best solution among them if there is more than one.

In this case, instead of stopping at the first attempt that provided a desired result,
we take note of it and continue in the attempts until all the solutions are found.

At the end, these are compared based on a given criterion,
which will determine which of them is to be considered the best.

Implementing gradient descent in Python

In this section, we will apply what we have learned so far on the gradient descent by completing a practical example.
We will define a function and then use that method to find the minimum point of the function.

"""

import numpy as np
import matplotlib.pyplot as plt


def grad_desc(x, y):
    Gradf = lambda x: 2 * x - 2

    ActualX = 3
    LearningRate = 0.01
    PrecisionValue = 0.000001
    PreviousStepSize = 1
    MaxIteration = 10000
    IterationCounter = 0

    while PreviousStepSize > PrecisionValue and IterationCounter < MaxIteration:
        PreviousX = ActualX
        ActualX = ActualX - LearningRate * Gradf(PreviousX)
        PreviousStepSize = abs(ActualX - PreviousX)
        IterationCounter = IterationCounter + 1
        print("Number of iterations = ", IterationCounter, "\nActual value of x  is = ", ActualX)

    print("X value of f(x) minimum = ", ActualX)


def plot_gd(x, y):
    fig = plt.figure()
    axdef = fig.add_subplot(1, 1, 1)
    axdef.spines['left'].set_position('center')
    axdef.spines['bottom'].set_position('zero')
    axdef.spines['right'].set_color('none')
    axdef.spines['top'].set_color('none')
    axdef.xaxis.set_ticks_position('bottom')
    axdef.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.show()


if __name__ == "__main__":
    x = np.linspace(-1, 3, 100)
    y = x ** 2 - 2 * x + 1
    grad_desc(x, y)
    plot_gd(x, y)
