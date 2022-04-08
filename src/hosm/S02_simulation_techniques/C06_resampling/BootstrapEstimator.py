"""
Bootstrap definition problem

Bootstrap is a statistical resampling technique with reentry
so that we can approximate the sample distribution of a statistic.

It therefore allows us to approximate the mean and variance of an estimator
so that we can build confidence intervals and calculate test p-values
when the distribution of the statistics of interest is not known.

Important Note
Bootstrap is based on the fact that the only available sample
is used to generate many more samples and to build the theoretical reference distribution.

Use the data from the original sample to calculate a statistic and
estimate its sample distribution without making any assumptions about the distribution model.

The plug-in principle is used to generate the distribution;
that is, the estimate of θ is constructed by substituting the
empirical equivalent of the unknown distribution function of the population.

The distribution function of the sample is obtained by constructing
a distribution of frequencies of all the values it can assume in that experimental situation.

In the simple case of simple random sampling, the operation is as follows.
Consider an observed sample with n elements, as described by the following equation:

x = (x 1 , . . . , x n )

From this distribution,
m other samples of a constant number equal to n,
say x * 1, ..., x * m, are resampled.

In each bootstrap extraction, the data from the first element of the sample can be extracted more than once.

Each one that's provided has a probability equal to 1 / n of being extracted.

Let E be the estimator of θ that interests us to study, say, E(x) = θ.

This quantity is calculated for each bootstrap sample,
E(x * 1),…, E(x * m).
In this way, m estimates of θ are available,
from which it is possible to calculate the bootstrap mean,
the bootstrap variance,
the bootstrap percentiles,
and so on.

These values are approximations of the corresponding unknown values and carry information on the distribution of E(x).
Therefore, starting from these estimated quantities,
it is possible to calculate confidence intervals, test hypotheses, and so on.

Bootstrap resampling using Python
We proceed in a similar way to what we did for Jackknife resampling.
We will generate a random distribution,
carry out a resampling according to the bootstrap method,
and then compare the results.
Let's see the code step by step in order to understand the procedure:
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def bootstrap():
    PopData = list()

    random.seed(7)

    for i in range(1000):
        DataElem = 50 * random.random()
        PopData.append(DataElem)

    PopSample = random.choices(PopData, k=100)

    PopSampleMean = list()
    for i in range(10000):
        SampleI = random.choices(PopData, k=100)
        PopSampleMean.append(np.mean(SampleI))

    MeanPopSampleMean = np.mean(PopSampleMean)
    print("The mean of the Bootstrap estimator is ", MeanPopSampleMean)

    MeanPopData = np.mean(PopData)
    print("The mean of the population is ", MeanPopData)

    MeanPopSample = np.mean(PopSample)
    print("The mean of the simple random sample is ", MeanPopSample)
    return PopSampleMean


def plot_bootstrap(PopSampleMean):
    plt.hist(PopSampleMean)
    plt.show()


if __name__ == "__main__":
    psm = bootstrap()
    plot_bootstrap(psm)
