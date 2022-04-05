"""
Linear congruential generator
One of the most common methods for generating random numbers is the Linear Congruence Generator (LCG).

The theory on which it rests is simple to understand and implement.

It also has the advantage of being computationally light.

The recursive relationship underlying this technique is provided by the following equation:

𝑥_𝑘+1 = ( 𝑎 ∗ 𝑥_𝑘 + 𝑐) mod 𝑚

• a is the multiplier (non-negative integers)
• c is the increment (non-negative integers)The pseudorandom number generator
• m is the mode (non-negative integers)
• x_0 is the initial value (seed or non-negative integers)

The modulo (mod), results in the remainder of the Euclidean division of the first number by the second.
For example, 18 mod 4 gives 2 as it is the remainder after division between the two numbers.

The linear congruence technique has the following characteristics:
• It is cyclical with a period that is approximately equal to m
• The generated numbers are discretized

To use this technique effectively, it is necessary to choose very large m values.
As an example, set the parameters of the method and generate the first 16 pseudorandom values.
Here is the Python code that allowed us to generate that sequence of numbers:
"""

import numpy as np


def LCG(max_iter=1000):
    a = 2
    c = 4
    m = 5
    x = 3
    for _ in range(max_iter):
        x = np.mod((a * x + c), m)
        yield x


if __name__ == "__main__":
    generator = LCG()
    for _ in range(1, 17):
        print(next(generator))
