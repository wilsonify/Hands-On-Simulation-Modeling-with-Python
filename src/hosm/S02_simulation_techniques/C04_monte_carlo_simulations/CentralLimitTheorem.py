"""
Central limit theorem
Monte Carlo not only allows us to obtain an estimate of the expected value,
as established by the law of large numbers,
but also allows us to estimate the uncertainty associated with it.

This is possible thanks to the central limit theorem,
which returns an estimate of the expected value and the reliability of that result.

The central limit theorem can be summarized with the following definition:
given a dataset with an unknown distribution, the sample's means will approximate the normal distribution.

If the law of large numbers tells us that the random variable allows us to evaluate the expected value,
the central limit theorem provides information on its distribution.

The interesting feature of the central limit theorem is that there are no constraints on the
distribution of the function used for the generation of the N samples, from which the random variable is formed.

In fact, it is not important what the distribution associated with the random variable is,
but when the average is characterized by a finite variance and is obtained for a very large number of samples,
it can be described through a Gaussian distribution.

Let's take a look at a practical example.
We generate 10,000 random numbers with a uniform distribution.
We then extract 100 samples from this population, also taken randomly.

We repeat this operation for a consistent number of times and for each time,
we evaluate its average and store this value in a vector.
In the end, we draw a histogram of the distribution that we have obtained.
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def plot_DataPop_hist(DataPop):
    plt.hist(DataPop, density=True, histtype='stepfilled', alpha=0.2)
    plt.show()


def plot_means(SamplesMeans):
    plt.figure()
    plt.hist(SamplesMeans, density=True, histtype='stepfilled', alpha=0.2)
    plt.show()


def clt():
    a = 1
    b = 100
    N = 10000
    DataPop = list(np.random.uniform(a, b, N))
    SamplesMeans = []
    for i in range(0, 1000):
        DataExtracted = random.sample(DataPop, k=100)
        DataExtractedMean = np.mean(DataExtracted)
        SamplesMeans.append(DataExtractedMean)


if __name__ == "__main__":
    clt()
