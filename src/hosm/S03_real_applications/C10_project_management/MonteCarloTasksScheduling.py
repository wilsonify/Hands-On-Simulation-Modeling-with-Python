"""
Scheduling project time using Monte

Carlo simulation Each project requires a time of realization,
and the beginning of some activities can be independent or dependent on previous activities ending.

Scheduling a project means determining the times of realization of the project itself.

A project is a temporary effort undertaken to create a unique product, service, or result.

The term project management refers to the application of knowledge, skills, tools, and techniques for the purpose of
planning, managing, and controlling a project and the activities of which it is composed.

The key figure in this area is the project manager,
who has the task and responsibility of coordinating and controlling the various components and actors involved,
with the aim of reducing the probability of project failure.

The main difficulty in this series of activities is to achieve the objectives set
in compliance with constraints such as the scope of the project, time, costs, quality, and resources.

In fact, these are limited aspects that are linked to each other and that need effective optimization.

The definition of these activities constitutes one of the key moments of the planning phase.

After defining what the project objectives are with respect to time, cost, and resources,
it is necessary to proceed with identifying and documenting the activities
that must be carried out to successfully complete the project.

For complex projects, it is necessary to create an ordered structure by decomposing
the project into simpler tasks.

For each task, it will be necessary to define activities and
execution times.

This starts with the main objective and breaks down the project to the
immediately lower level in all those deliverables or main sub-projects that make it up.
These will, in turn, be broken down.

This will continue until you are satisfied with the
degree of detail of the resulting final items.

Each breakdown results in a reduction in the
size, complexity, and cost of the interested party.

Defining the scheduling grid
A fundamental part of all project management is constructing the scheduling grid.
This
is an oriented graph that represents the temporal succession and the logical dependencies
between the activities involved in the realization of the project.

In addition to constructing
the grid, the scheduling process also determines the start and end times of activities based
on factors such as duration, resources, and so on.

In the example we are dealing with, we will take care of evaluating the times necessary for
the realization of a complex project.

Let's start by defining the scheduling grid. Suppose
that, by decomposing the project structure, we have defined six tasks. For each task, the
activities, the personnel involved, and the time needed to finish the job were defined.

Some tasks must be performed in a series, in the sense that the activities of the previous
task must be completed so that they can start those of the next task.

Others, however, can be performed in parallel, in the sense that two teams can simultaneously work on two
different tasks to reduce project delivery times.

This sequence of tasks is defined in the scheduling grid, as follows:

The preceding diagram shows us that the first two tasks develop in parallel, which means
that the time required to finish these two tasks will be provided by the time-consuming
task. The third task develops in a series, while the next two are, again, in parallel.

The last task is still in the series.
This sequence will be necessary when we evaluate the project times.

Estimating the task's time
The duration of these tasks is often difficult to estimate due to the number of factors that
can influence it: the availability and/or productivity of the resources, the technical and
physical constraints between the activities, and the contractual commitments.

Expert advice, supported by historical information, can be used wherever possible.

The members of the project team will also be able to provide information on the duration or
the maximum recommended limit for the duration for the task by deriving information from similar projects.

There are several ways we can estimate tasks.
In this example, we will use three-point estimation.

In three-point estimation, the accuracy of the duration of the activity estimate
can be increased in terms of the amount of risk in the original estimate.

Three-point estimates are based on determining the following three types of estimates:

• Optimistic:
The duration of the activity is based on the best scenario in relation to
what is described in the most probable estimate. This is the minimum time it will take to complete the task.

• Pessimistic: The duration of the activity is based on the worst-case scenario in
relation to what is described in the most probable estimate. This is the maximum
time that it will take to complete the task.

• More likely: The duration of the activity is based on realistic expectations in terms
of availability for the planned activity.
A first estimate of the duration of the activity can be constructed using an average of the
three estimated durations.

This average typically provides a more accurate estimate of the
duration of the activity than a more likely single value estimate. But that's not what we
want to do.

Suppose that the project team used three-point estimation for each of the six tasks. The
following table shows the times proposed by the team:

After defining the sequence of tasks and the time it will take to perform each individual
task, we can develop an algorithm for estimating the overall time of the project.

Developing an algorithm for project scheduling
In this section, we will analyze an algorithm for scheduling a project based on the Monte
Carlo simulation.
"""

import random

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def mcts():
    N = 10000
    TotalTime = []
    T = np.empty(shape=(N, 6))
    TaskTimes = [
        [3, 5, 8],
        [2, 4, 7],
        [3, 5, 9],
        [4, 6, 10],
        [3, 5, 9],
        [2, 6, 8]
    ]
    nTaskTimes = len(TaskTimes)
    print(f"nTaskTimes = {nTaskTimes}")
    Lh = []
    for i in range(nTaskTimes):
        # generate the separation value of the triangular distribution
        Lh.append((TaskTimes[i][1] - TaskTimes[i][0]) / (TaskTimes[i][2] - TaskTimes[i][0]))

    for p in range(N):
        for i in range(nTaskTimes):
            # simulation to generate variations according to the triangular distribution
            trand = random.random()
            if trand < Lh[i]:
                T[p][i] = TaskTimes[i][0] + np.sqrt(
                    trand * (TaskTimes[i][1] - TaskTimes[i][0]) * (TaskTimes[i][2] - TaskTimes[i][0]))
            else:
                T[p][i] = TaskTimes[i][2] - np.sqrt(
                    (1 - trand) * (TaskTimes[i][2] - TaskTimes[i][1]) * (TaskTimes[i][2] - TaskTimes[i][0]))
        TotalTime.append(T[p][0] + np.maximum(T[p][1], T[p][2]) + np.maximum(T[p][3], T[p][4]) + T[p][5])

    Data = pd.DataFrame(T, columns=['Task1', 'Task2', 'Task3', 'Task4', 'Task5', 'Task6'])

    pd.set_option('display.max_columns', None)
    print(Data.describe())

    print("Minimum project completion time = ", np.amin(TotalTime))
    print("Mean project completion time = ", np.mean(TotalTime))
    print("Maximum project completion time = ", np.amax(TotalTime))
    return Data


def plot_mcts(Data):
    Data.hist(bins=10)
    plt.show()


if __name__ == "__main__":
    data = mcts()
    plot_mcts(data)
