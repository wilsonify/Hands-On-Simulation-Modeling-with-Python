"""
As the number of independent experiments that are carried out increases,
the binomial distributions approach a curve called the bell curve or Gauss curve.
The normal distribution, also called the Gaussian distribution, is the most used continuous distribution in statistics.
Normal distribution is important in statistics for the following fundamental reasons:

• Several continuous phenomena seem to follow, at least approximately, a normal distribution.
• The normal distribution can be used to approximate numerous discrete probability distributions.
• The normal distribution is the basis of classical statistical inference by virtue of the central limit theorem.80

Normal distribution has some important characteristics:
• The normal distribution is symmetrical and bell-shaped.
• Its central position measures – the expected value and the median – coincide.
• Its interquartile range is 1.33 times the mean square deviation.
• The random variable in the normal distribution takes values between -∞ and + ∞.

In the case of a normal distribution, the normal probability density function is given by
the following equation:
𝑓(𝑋) = 1/√(2𝜋𝜎) * 𝑒^( −(1/2)[(𝑋−𝜇)/𝜎]^2)

Here, we have the following:
• 𝜇 is the expected value.
• 𝜎 is the standard deviation.

Note that, since e and π are mathematical constants, the probabilities of a normal
distribution depend only on the values assumed by the parameters µ and σ.
Now, let's learn how to generate a normal distribution in Python. Let's start as always by
importing the necessary libraries:
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    mu = 10
    sigma = 2

    P1 = np.random.normal(mu, sigma, 1000)

    mu = 5
    sigma = 2

    P2 = np.random.normal(mu, sigma, 1000)

    mu = 15
    sigma = 2

    P3 = np.random.normal(mu, sigma, 1000)

    Plot1 = sns.distplot(P1)
    Plot2 = sns.distplot(P2)
    Plot3 = sns.distplot(P3)

    mu = 10
    sigma = 2

    P4 = np.random.normal(mu, sigma, 1000)

    mu = 10
    sigma = 1

    P5 = np.random.normal(mu, sigma, 1000)

    mu = 10
    sigma = 0.5

    P6 = np.random.normal(mu, sigma, 1000)

    plt.figure()
    Plot4 = sns.distplot(P4)
    Plot5 = sns.distplot(P5)
    Plot6 = sns.distplot(P6)
    plt.show()
