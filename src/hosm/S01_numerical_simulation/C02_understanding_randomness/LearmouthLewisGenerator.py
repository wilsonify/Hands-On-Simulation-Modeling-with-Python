"""
Random numbers with uniform distribution

A sequence of numbers uniformly distributed between [0, 1] can be obtained using the
following formula:

𝑈_𝑛 = 𝑋_𝑛 / 𝑚

The obtained sequence is periodic, with a period less than or equal to m.

If the period is m, then it has a full period.

This occurs when the following conditions are true:
• If m and c have prime numbers
• If m is divisible by a prime number, b, for which it must also be divisible
• If m is divisible by 4, then a - 1 must also be divisible by 4

note:
By choosing a large value of m,
you can reduce both the phenomenon of periodicity and the problem of generating rational numbers.
Furthermore, it is not necessary for simulation purposes that all numbers between [0, 1] are generated, because these are infinite.

However, it is necessary that as many numbers as possible within the range have the same probability of being generated.

Generally, a value of m is m ≥ 109 so that the generated numbers constitute a dense subset of the interval, [0, 1].

An example of a multiplicative generator that is widely used in 32-bit computers is the
Learmonth-Lewis generator.

This is a generator in which the parameters assume the following values:
• a = 75
• c = 0
• m = 2^31 – 1

Let's analyze the code that generates the first 100 random numbers according to this method:
"""

import numpy as np


def LLG(iter_max=1000):
    a = 75
    c = 0
    m = 2 ** 31 - 1
    x = 0.1
    for _ in range(iter_max):
        x = np.mod((a * x + c), m)
        u = x / m
        yield u


if __name__ == "__main__":
    generator = LLG()
    for i in range(1, 100):
        print(next(generator))
