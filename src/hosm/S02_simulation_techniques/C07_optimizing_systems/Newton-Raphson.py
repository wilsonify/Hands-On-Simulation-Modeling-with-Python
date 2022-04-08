"""
Approaching Newton-Raphson for numerical optimization

The Newton-Raphson method is also used for solving numerical optimization problems.
In this case, the method takes the form of Newton's method for finding the zeros of a function,
but applied to the derivative of the function f.

This is because determining the minimum point of the
function f is equivalent to determining the root of the first derivative f '.

In this case, the update formula takes the following form:

𝑥_𝑛+1 = 𝑥_𝑛 − 𝑓′(𝑥_𝑛)/𝑓′′(𝑥_𝑛)


In the previous equation, we have the following:

• 𝑓′(𝑥_𝑛) is the first derivative of the function f
• 𝑓′′(𝑥_𝑛) is the second derivative of the function f

Important Note
The Newton-Raphson method is usually preferred over the descending gradient method due to its speed.
However,
it requires knowledge of the analytical expression of the first and second derivatives and
converges indiscriminately to the minima and maxima.

There are variants that bring this method to global convergence and
that lower the computational cost by avoiding having to determine the direction of the research with direct methods.

Applying the Newton-Raphson technique

In this section,
we will apply what we have learned so far about the Newton-Raphson method by completing a practical exercise.
We'll define a function and then use that method to find the minimum point of the function.

"""

import numpy as np
import matplotlib.pyplot as plt


def nr(x, y):
    print('Value of x at the minimum of the function', x[np.argmin(y)])

    FirstDerivative = lambda x: 3 * x ** 2 - 4 * x - 1
    SecondDerivative = lambda x: 6 * x - 4

    ActualX = 3
    PrecisionValue = 0.000001
    PreviousStepSize = 1
    MaxIteration = 10000
    IterationCounter = 0

    while PreviousStepSize > PrecisionValue and IterationCounter < MaxIteration:
        PreviousX = ActualX
        ActualX = ActualX - FirstDerivative(PreviousX) / SecondDerivative(PreviousX)
        PreviousStepSize = abs(ActualX - PreviousX)
        IterationCounter = IterationCounter + 1
        print("Number of iterations = ", IterationCounter, "\nActual value of x  is = ", ActualX)

    print("X value of f(x) minimum = ", ActualX)


def plot_nr(x, y):
    fig = plt.figure()
    axdef = fig.add_subplot(1, 1, 1)
    axdef.spines['left'].set_position('center')
    axdef.spines['bottom'].set_position('zero')
    axdef.spines['right'].set_color('none')
    axdef.spines['top'].set_color('none')
    axdef.xaxis.set_ticks_position('bottom')
    axdef.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.show()


if __name__ == "__main__":
    x = np.linspace(0, 3, 100)
    y = x ** 3 - 2 * x ** 2 - x + 2
    nr(x, y)
    plot_nr(x, y)
