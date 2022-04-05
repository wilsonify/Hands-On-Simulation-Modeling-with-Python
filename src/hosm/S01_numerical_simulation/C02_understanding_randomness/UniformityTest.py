"""
Uniformity test

After having generated the pseudorandom numerical sequence,
it is necessary to verify the goodness of the obtained sequence.

It is a question of checking whether the sequence obtained,
which constitutes a random sample of the experiment, follows a uniform distribution.

To carry out this check, we can use the χ2 test (chi-squared test).
Let's demonstrate how to do this.

The first operation is to divide the interval, [0, 1], into s subintervals of the same length.
Then, we count how many numbers of the generated sequence are included in the i-th interval,
as follows:

𝑅_𝑖 = { 𝑥_𝑖 | 𝑥_𝑗 ∈ 𝑠_𝑖 , 𝑗 = 1, … 𝑁}

The R_i values should be as close as possible to the N/s value.
If the sequence were perfectly uniform,
then each sub-interval would have the same number of samples in the sequence.

We indicate, with V, the variable to perform the test.
This variable is calculated using the following formula:
𝑉 = ∑ (as i goes from 1 to s) ( R_i - (N/S) )^2 / ( N/S )

After introducing the tools that allow us to perform a uniformity test,
let's analyze a practical example that will help us to understand how to carry out this procedure.
We generate a pseudorandom numerical sequence of 100 values, by means of the congruent linear generator,
by fixing the parameters as follows:
• a = 75
• c = 0
• m = 2^31 – 1

This is the random number generator already seen in the Lagged Fibonacci generator section.
We have already introduced the code that allows us to generate the sequence,
so let's modify it for our new requirements by storing the sequence in an array:
"""

import numpy as np


def LCG2():
    a = 75
    c = 0
    m = 2 ** 31 - 1
    x = 0.1
    for _ in range(1000):
        x = np.mod((a * x + c), m)
        u = x / m
        yield u


def LFG2():
    u_nda = np.array([])
    generator = LCG2()
    for i in range(0, 100):
        u_nda = np.append(u_nda, next(generator))

    N = 100
    s = 20
    Ns = N / s
    S = np.arange(0, 1, 0.05)
    _counts = np.empty(S.shape, dtype=int)
    _V = 0
    for i in range(0, 20):
        _counts[i] = len(np.where((u_nda >= S[i]) & (u_nda < S[i] + 0.05))[0])
        _V = _V + (_counts[i] - Ns) ** 2 / Ns
    Yposition = np.arange(len(_counts))
    return _counts, Yposition, _V



if __name__ == "__main__":
    import matplotlib.pyplot as plt

    counts, Ypos, V = LFG2()
    plt.bar(Ypos, counts)
    plt.show()
