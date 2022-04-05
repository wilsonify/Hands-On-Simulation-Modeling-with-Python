"""
Lagged Fibonacci generator

The lagged Fibonacci algorithm for generating pseudorandom numbers arises from the attempt to generalize the method of linear congruences.
One of the reasons that led to the search for new generators was the need,
useful for many applications especially in parallel computing, to lengthen the generator period.

The period of a linear generator when m is approximately 109 is enough for many applications, but not all of them.
One of the techniques developed is to make X_n + 1 dependent on the two previous values, X_n and X_(n − 1) ,

instead of only on X_n , as is the case in the LCG method.
In this case, the period may arrive close to the value, m 2 ,
because the sequence will not repeat itself until the following equality is obtained:

( 𝑋_𝑛+𝜆 , 𝑋_𝑛+𝜆+1 ) = (  𝑋_𝑛 , 𝑋_𝑛+1 )

The simplest generator of this type is the Fibonacci sequence represented by the following equation:
𝑋_𝑛+1 = ( 𝑋_𝑛 + 𝑋_𝑛−1 ) mod 𝑚

This generator was first analyzed in the 1950s and provides a period, m,
but the sequence does not pass the simplest statistical tests.
We then tried to improve the sequence using the following equation:
𝑋_𝑛+1 = ( 𝑋_𝑛 + 𝑋_𝑛−𝑘 ) mod 𝑚

This sequence, although better than the Fibonacci sequence, does not return satisfactory results.

We had to wait until 1958, when Mitchell and Moore proposed the following sequence:
𝑋_𝑛 = (𝑋_𝑛−24 + 𝑋_𝑛−55 ) mod 𝑚, 𝑛 ≥ 55

Here, m is even and X_0 , ... X_54 are arbitrary integers that are not all even.
Constants 24 and 55 are not chosen at random but are numbers that define a sequence whose least significant bits (X n mod 2) have a period of length 2^55 -1.
Therefore, the sequence ( X_n ) must have a period of length of at least 2^55 - 1.
The succession has a period of 2^M -1 (2 55 -1) where m = 2^M .
Numbers 24 and 55 are commonly called lags and the sequence ( X_n ) is called a Lagged Fibonacci Generator (LFG). 

The LFG sequence can be generalized with the following equation:
𝑋_𝑛 = (𝑋_𝑛−𝑙 ⊗ 𝑋_𝑛−𝑘 ) mod 2^𝑀 , 𝑙 > 𝑘 > 0

Here, ⊗ refers to any of the following operations: +, −, ×, or ⊗ (exclusive or).

Only some pairs (k, l) give sufficiently long periods. 
In these cases, the period is 2 M -1 (2 l -1). 
The pairs (k, l) must be chosen appropriately. 
The only condition on the first l values is that at least one of them must be odd; 
otherwise, the sequence will be composed of even numbers.
Let's look at how to implement a simple example of additive LFG in Python using the
following parameters: x0 = x1 = 1 and m = 2 32 . Here is the code to generate the first 100 random numbers:
"""

import numpy as np


def LFG(max_iter=1000):
    x0 = 1
    x1 = 1
    m = 2 ** 32
    for _ in range(max_iter):
        x = np.mod((x0 + x1), m)
        x0 = x1
        x1 = x
        yield x


if __name__ == "__main__":
    generator = LFG()
    for i in range(101):
        print(next(generator))
