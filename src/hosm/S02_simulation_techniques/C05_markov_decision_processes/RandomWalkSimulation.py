"""
Simulating a one-dimensional random walk

The simulation of a casual walk does not represent a trivial succession of random numbers
since the next step to the current one represents its evolution.

The dependence between the next two steps guarantees a certain consistency from one passage to the next.

This is not guaranteed in a banal generation of independent random numbers,
which instead return big differences from one number to another.

Let's learn how to represent the sequence of actions to be performed in a simple casual walking model through the
following pseudocode:
1. Start from the 0 position.
2. Randomly select a dichotomous value (-1, 1).
3. Add this value to the previous time step.
4. Repeat step 2 onward.

This simple iterative process can be implemented in Python by processing a list of 1,000 time steps for the random walk.
Let's take a look:
"""
from random import seed
from random import random
from matplotlib import pyplot


def rw():
    seed(1)
    RWPath = list()
    RWPath.append(-1 if random() < 0.5 else 1)
    for i in range(1, 1000):
        ZNValue = -1 if random() < 0.5 else 1
        XNValue = RWPath[i - 1] + ZNValue
        RWPath.append(XNValue)
    return RWPath


def plot_rw(RWPath):
    pyplot.plot(RWPath)
    pyplot.show()


if __name__ == "__main__":
    walk = rw()
    plot_rw(walk)
