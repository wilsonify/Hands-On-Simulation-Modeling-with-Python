"""
Estimating the coefficient of variation

To make comparisons regarding variability between different distributions,
we can use the coefficient of variation (CV) since it considers the average of the distribution.

The variation coefficient is a relative measure of dispersion and is a dimensionless magnitude.

It allows us to evaluate the dispersion of the values around the average, regardless of the unit of measurement.

Important Note
For example, the standard deviation of a sample of income expressed in dollars is completely different
from the standard deviation of the same income expressed in euros,
while the dispersion coefficient is the same in both cases.

The coefficient of variation is calculated using the following equation:

CV = 𝜎  ∗ 100 / |𝜇|

In the previous equation, we use the following parameters:
• 𝜎 is the standard deviation of the distribution.
• |𝜇| is the absolute value of the mean of the distribution.


The variance is the average of the differences squared between each of the observations in a group of data
and the arithmetic mean of the data:

So, it represents the squared error that we commit,
on average, replacing a generic observation x i with the average µ.

The standard deviation is the square root of the variance and therefore
represents the square root of the mean squared error:

The CV, which can be defined starting from the average and standard deviation,
is the appropriate index for comparing the variability of two characters.
CV is particularly useful when you want to compare the dispersion of data with different units
of measurement or with different ranges of variation.
"""

import random
import statistics
import matplotlib.pyplot as plt


def CVCalc(Dat):
    CVCalc = statistics.stdev(Dat) / statistics.mean(Dat)
    return CVCalc


def jackknife_cv():
    PopData = list()

    random.seed(5)

    for i in range(100):
        DataElem = 10 * random.random()
        PopData.append(DataElem)

    CVPopData = CVCalc(PopData)
    print(CVPopData)

    N = len(PopData)
    JackVal = list()
    PseudoVal = list()
    for i in range(N - 1):
        JackVal.append(0)
    for i in range(N):
        PseudoVal.append(0)

    for i in range(N):
        for j in range(N):
            if (j < i):
                JackVal[j] = PopData[j]
            else:
                if (j > i):
                    JackVal[j - 1] = PopData[j]
        PseudoVal[i] = N * CVCalc(PopData) - (N - 1) * CVCalc(JackVal)

    MeanPseudoVal = statistics.mean(PseudoVal)
    print(MeanPseudoVal)
    VariancePseudoVal = statistics.variance(PseudoVal)
    print(VariancePseudoVal)
    VarJack = statistics.variance(PseudoVal) / N
    print(VarJack)
    return PseudoVal


def plot_jk(PseudoVal):
    plt.hist(PseudoVal)
    plt.show()


if __name__ == "__main__":
    pv = jackknife_cv()
    plot_jk(pv)
