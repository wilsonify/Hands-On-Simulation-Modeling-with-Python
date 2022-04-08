"""
Understanding the geometric Brownian motion model

The name Brownian comes from the Scottish botanist Robert Brown who,
in 1827, observed, under the microscope,
how pollen particles suspended in water moved continuously in a random and unpredictable way.

In 1905, it was Einstein who gave a molecular interpretation of the phenomenon of movement observed by Brown.
He suggested that the motion of the particles was mathematically describable,
assuming that the various jumps were due to the random collisions of pollen particles with water molecules.

Today, Brownian motion is, above all, a mathematical tool in the context of probability theory.
This mathematical theory has been used to describe an ever-widening set of phenomena,
studied by disciplines that are very different from physics.

For instance, the prices of financial securities,
the spread of heat,
animal populations,
bacteria,
illness,
sound, and light
are modeled using the same instrument.


Important note
Brownian motion is a phenomenon that consists of the uninterrupted and irregular movement
made by small particles or grains of colloidal size, that is,
particles that are far too small to be observed with the naked eye but
are significantly larger than atoms when immersed in a fluid.

Defining a standard Brownian motion
There are various ways of constructing a Brownian motion model and various equivalent definitions of Brownian motion.

Let's start with the definition of a standard Brownian motion (the Wiener process).

The essential properties of a standard Brownian motion include the following:
• The standard Brownian motion starts from zero.
• The standard Brownian motion takes a continuous path.
• The increases suffered by the Brownian process are independent.
• The increases suffered by the Brownian process in the time interval, dt, indicate a
Gaussian distribution, with an average that is equal to zero and a variance that is
equal to the time interval, dt.


Based on these properties, we can consider the process as the sum of a large number of extremely small increments.

After choosing two instants, t and s, the random variable, Y (s) -Y (t), follows a normal distribution,
with a mean of (s-t) and variance of 2 (s-t), which we can represent using the following equation:
𝑌𝑌(𝑠𝑠) − 𝑌𝑌(𝑡𝑡)~𝒩𝒩(𝜇𝜇 (𝑠𝑠 − 𝑡𝑡), 𝜎𝜎 2 (𝑠𝑠 − 𝑡𝑡))

The hypothesis of normality is very important in the context of linear transformations.
In fact, the standard Brownian motion takes its name from the type of distribution
that is a standard normal distribution, with parameters of = 0 and 2 = 1.

Therefore, it can be said that the Brownian motion, Y (t), with a unit mean and variance
can be represented as a linear transformation of a standard Brownian motion, according to the following equation:
𝑌𝑌(𝑡𝑡) = 𝑌𝑌(0) + 𝜇𝜇 ∗ 𝑡𝑡 + 𝜎𝜎 ∗ 𝑍𝑍(𝑡𝑡)

In the previous equation, we can observe the following:
• ( ) is the standard Brownian motion.

Using Simulation Models for Financial Engineering
The weak point of this equation lies in the fact that the
probability that Y (t) assuming a negative value is positive;
in fact, since Z (t) is characterized by independent increments,
which can assume a negative sign,
the risk of the negativity of Y (t) is not zero.

Now, consider the Brownian motion (the Wiener process) for sufficiently small time intervals.

An infinitesimal increment of this process is obtained in the following form:
𝑍𝑍 (𝑡𝑡+𝑑𝑑𝑑𝑑) − 𝑍𝑍 (𝑡𝑡) = 𝛿𝛿𝑍𝑍 𝑡𝑡 = 𝑁𝑁 ∗ √𝑑𝑑𝑑𝑑

The previous equation can be rewritten as follows:
𝑍𝑍 (𝑡𝑡+𝑑𝑑𝑑𝑑) − 𝑍𝑍 (𝑡𝑡)
𝑁𝑁
=
𝑑𝑑𝑑𝑑
√𝑑𝑑𝑑𝑑

This process is not limited in variation and therefore,
cannot be differentiated in the context of classical analysis.

In fact, the previous one tends to infinity for the interval, dt.
Addressing the Wiener process as random walk A Wiener process can be considered a borderline case of random walk.

We dealt with a random walk in Chapter 5, Simulation-Based Markov Decision Processes.

We have seen that the position of a particle at instant n will be represented by the following equation:
𝑌𝑌 𝑛𝑛 = 𝑌𝑌 𝑛𝑛−1 + 𝑍𝑍 𝑛𝑛 ;
𝑛𝑛 = 1,2, …

In the previous formula, we can observe the following:
• Y n is the next value in the walk.
• Y n-1 is the observation in the previous time phase.
• Z n is the random fluctuation in that step.

If the n random numbers, Z n , have a mean equal to zero and a variance equal to 1,
then, for each value of n, we can define a stochastic process using the following equation:
𝑌𝑌 𝑛𝑛 (𝑡𝑡) =
1
√𝑛𝑛
∗ ∑ 𝑍𝑍 𝑘𝑘
𝑘𝑘

The preceding formula can be used in an iterative process.

For very large values of n, we can write the following:
𝑌𝑌 𝑛𝑛 (𝑠𝑠) − 𝑌𝑌 𝑛𝑛 (𝑡𝑡) ~ 𝒩𝒩(0, (𝑠𝑠 − 𝑡𝑡))

The previous formula is due to the central limit theorem that we covered in Chapter 4, Monte Carlo Simulations.
Implementing a standard Brownian motion So,
let's demonstrate how to generate a simple Brownian motion in the Python environment.
Let's start with the simplest case, in which we define the time interval,
the number of steps to be performed, and the standard deviation:
"""
import numpy as np
import matplotlib.pyplot as plt


def sbm():
    np.random.seed(4)
    n = 1000
    SQN = 1 / np.math.sqrt(n)
    ZValues = np.random.randn(n)
    Yk = 0
    SBMotion = list()
    for k in range(n):
        Yk = Yk + SQN * ZValues[k]
        SBMotion.append(Yk)
    return SBMotion


def plot_sbm(SBMotion):
    plt.plot(SBMotion)
    plt.show()


if __name__ == "__main__":
    sb = sbm()
    plot_sbm(sb)
