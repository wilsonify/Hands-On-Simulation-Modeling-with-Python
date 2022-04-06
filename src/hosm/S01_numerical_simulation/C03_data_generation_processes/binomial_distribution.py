"""
Binomial distribution
In many situations, we are interested in checking whether a certain characteristic occurs or not.
This corresponds to an experiment with only two possible outcomes-also
called a dichotomous-that can be modeled with a random variable X that assumes value 1
(success) with probability p and value 0 (failure) with probability 1-p, with 0 <p < 1,
as follows:
𝑋 =  1, p; 0, 1-p

The expected value and variance of X are calculated as follows:
𝐸(𝑋) = 0 ∗ (1 − 𝑝) + 1 ∗ 𝑝 = 𝑝


𝜎^2 = 𝐸(𝑋^2) − (𝐸(𝑋))^2 = (0^2 ∗ (1 − 𝑝) + 1^2 ∗ 𝑝) − 𝑝^2 = 𝑝 ∗ (1 − 𝑝)

The binomial distribution is the probability of obtaining x successes in n independent trials.
The probability density for the binomial distribution is obtained using the following equation:


𝑃_𝑥 = ( n choose x ) 𝑝^𝑥 𝑞^(𝑛−𝑥) , 0 ≤ 𝑥 ≤ 𝑛

Here, we have the following:
• P x is the probability density
• n is the number of independent experiments
• x is the number of successes
• p is the probability of success
• q is the probability of fail

Now, let's look at a practical example.
We throw a dice n = 10 times.
In this case we want to study the binomial variable x = number of times a number <= 3 came out.
We define the parameters of the problem as follows:

𝑛 = 10
0 ≤ 𝑥 ≤ 𝑛

𝑝 = 3/6 = 0.5
𝑞 = 1 − 𝑝 = 0.5

We then evaluate the probability density function with Python code, as follows:
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000
n = 10
p = 0.5

if __name__ == "__main__":
    P1 = np.random.binomial(n, p, N)

    plt.figure()
    plt.hist(P1, density=True, alpha=0.8, histtype='bar', color='green', ec='black')
    plt.show()
