"""
Introducing the random module
The random module implements PRNGs for various distributions.
The random module is based on the Mersenne Twister algorithm,
which was originally developed to produce inputs for Monte Carlo simulations.
The Mersenne Twister algorithm is a PRNG that produces almost uniform numbers suitable for a wide range of applications.
It is important to note that random numbers are generated using repeatable and predictable deterministic algorithms.
They begin with a certain seed value and, every time we ask for a new number, we get one based on the current seed.
The seed is an attribute of the generator.
If we invoke the generator twice with the same seed,
the sequence of numbers that will be generated starting from that seed will always be the same.
However, these numbers will be evenly distributed.
Let's analyze, in detail, the functions contained in the module through a series of practical examples.
"""

import random

CitiesList = [
    'Rome',
    'New York',
    'London',
    'Berlin',
    'Moskov',
    'Los Angeles',
    'Paris',
    'Madrid',
    'Tokio',
    'Toronto'
]

DataList = range(10, 100, 10)

if __name__ == "__main__":

    for i in range(20):
        print('%05.4f' % random.random(), end=' ')
    print()

    random.seed(1)

    for i in range(20):
        print('%05.4f' % random.random(), end=' ')
    print()

    for i in range(20):
        print('%6.4f' % random.uniform(1, 100), end=' ')
    print()

    for i in range(20):
        print(random.randint(-100, 100), end=' ')
    print()

    for i in range(20):
        print(random.randrange(0, 100, 5), end=' ')
    print()

    for i in range(10):
        CitiesItem = random.choice(CitiesList)
        print("Randomly selected item from Cities list is - ", CitiesItem)

    print("Initial Data List = ", DataList)
    DataSample = random.sample(DataList, k=5)
    print("Sample Data List = ", DataSample)
