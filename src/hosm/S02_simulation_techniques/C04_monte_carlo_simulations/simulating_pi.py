"""
Applying the Monte Carlo method for Pi estimation
The Monte Carlo method is a problem-solving strategy that uses statistics.
If we indicate with P the probability of a certain event,
then we can randomly simulate this event and obtain P
 by finding the ratio between the number of times our event occurred and the number of total simulations,
 as follows:

 𝑃 = number of event occurrences / number of total simulations


We can apply this strategy to get an approximation of Pi. Pi (π) is a mathematical constant
indicating the relationship between the length of a circumference and its diameter.
In fact, if we denote by C the length of a circumference and by d its diameter, we know that C = d * π.

The length of a circumference with a diameter equal to 1 is worth π.

Important Note
Usually, we approximate the value of Pi with 3.14 to simplify the accounts.
However, π is an irrational number; that is, it has an infinite number of digits
after the decimal point that never repeat on a regular basis.
Given a circle of radius 1, it can be inscribed in a square of length 2.
For convenience, we will only consider a fraction of the circle.

we can see that the area of the square in blue is 1 and that the area of the circular sector in yellow
(1/4 of the circle) is instead pi / 4.
We randomly place a very large number of points inside the square.
Thanks to the very large number and random distribution,
we can approximate the size of the areas with the number of points contained in them.

If we generate N random numbers inside the square, the number of points that fall in the circular sector,
which we will denote by M, divided by the total number of generated numbers, N,
we will have to approximate the area of the circular sector and therefore it will be equal to Pi/4.
From this, we can derive the following equation:

𝜋 = 4 ∗ 𝑀 / 𝑁

The greater the number of points generated, the more precise the approximation of Pi will be.
Now, let's estimate Pi:
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt


def estimate_pi():
    N = 10000
    M = 0

    XCircle = []
    YCircle = []
    XSquare = []
    YSquare = []

    for p in range(N):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2 <= 1):
            M += 1
            XCircle.append(x)
            YCircle.append(y)
        else:
            XSquare.append(x)
            YSquare.append(y)

    Pi = 4 * M / N

    print("N=%d M=%d Pi=%.2f" % (N, M, Pi))

    XLin = np.linspace(0, 1)
    YLin = []
    for x in XLin:
        YLin.append(math.sqrt(1 - x ** 2))
    return Pi


def plot_pi(XLin, YLin, XCircle, YCircle, XSquare, YSquare):
    plt.axis("equal")
    plt.grid(which="major")
    plt.plot(XLin, YLin, color="red", linewidth="4")
    plt.scatter(XCircle, YCircle, color="yellow", marker=".")
    plt.scatter(XSquare, YSquare, color="blue", marker=".")
    plt.title("Monte Carlo method for Pi estimation")
    plt.show()


if __name__ == "__main__":
    pi = estimate_pi()
    print(f"Pi={pi:.2f}")
