"""
Uniform distribution
The simplest of the continuous variable probability distribution functions is the one in which
the same degree of confidence is assigned to all the possible values of a variable defined in a certain range.
Since the probability density function is constant, the distribution function is linear.
The uniform distribution is used to treat measurement errors whenever they occur
with certainty that a certain variable is contained in a certain range,
but there is no reason to believe some values are more plausible than others.
Using suitable techniques, starting from a uniformly distributed variable,
it is possible to build other variables that have been distributed at will.
Now, let's start practicing using it.
We will start by generating a uniform distribution of random numbers contained in a specific range.
To do this, we will use the numpy random.uniform() function.
This function generates random values uniformly distributed over the half-open interval [a, b);
that is, it includes the first, but excludes the second.
Any value within the given interval is equally likely to be drawn by uniform distribution:
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a = 1
    b = 100
    N = 100

    X1 = np.random.uniform(a, b, N)
    plt.plot(X1)
    plt.show()
    plt.figure()
    plt.hist(X1, density=True, histtype='stepfilled', alpha=0.2)
    plt.show()

    a = 1
    b = 100
    N = 10000
    X2 = np.random.uniform(a, b, N)

    plt.figure()
    plt.plot(X2)
    plt.show()

    plt.figure()
    plt.hist(X2, density=True, histtype='stepfilled', alpha=0.2)
    plt.show()
