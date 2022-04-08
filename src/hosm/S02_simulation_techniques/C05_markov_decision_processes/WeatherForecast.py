"""
Simulating a weather forecast

Another potential application of Markov chains is in the development of a weather forecasting model.

Let's learn how to implement this algorithm in Python .

To start, we can work with a simplified model:
we will consider only two climatic conditions/states, that is, sunny and rainy.
Our model will assume that tomorrow's weather conditions will be affected by today's weather conditions,
making the process take on Markovian characteristics.

This link between the two states will be represented by the following transition matrix:
𝑃𝑃 = [0.80 0.20; 0.25 0.75]

The transition matrix returns the conditional probabilities P (A | B),
which indicate the probability that event A occurs after event B has occurred.

This matrix therefore contains the following conditional probabilities:
𝑃𝑃 = [ 𝑃(Sunny|Sunny) 𝑃(Sunny|Rainy); 𝑃𝑃(Rainy|Sunny) 𝑃(Rainy|Rainy)]

In the previous transition matrix, each row contains a complete distribution.
Therefore, all the numbers must be non-negative and the sum must be equal to 1.

The climatic conditions show a tendency to resist change.
For this reason, after a sunny day,
the probability of another sunny – P (Sunny | Sunny) – day is greater than a rainy – P (Sunny | Rainy) day.

The climatic conditions of tomorrow are not directly related to those of yesterday;
it follows that the process is Markovian.

The simulation model we want to elaborate on will have to calculate the probability that
it will rain in the next few days.

It will also have to allow you to recover a statistic of the proportion of sunny and rainy days
in a certain period of time.

The process, as mentioned previously, is Markovian,
and the tools we analyzed in the previous sections allow us to obtain the requested information.
Let's get started:
"""

import numpy as np
import matplotlib.pyplot as plt


def weather():
    np.random.seed(3)
    StatesData = ["Sunny", "Rainy"]

    TransitionStates = [["SuSu", "SuRa"], ["RaRa", "RaSu"]]
    TransitionMatrix = [[0.80, 0.20], [0.25, 0.75]]

    WeatherForecasting = list()
    NumDays = 365
    TodayPrediction = StatesData[0]

    print("Weather initial condition =", TodayPrediction)

    for i in range(1, NumDays):

        if TodayPrediction == "Sunny":
            TransCondition = np.random.choice(TransitionStates[0], replace=True, p=TransitionMatrix[0])
            if TransCondition == "SuSu":
                pass
            else:
                TodayPrediction = "Rainy"



        elif TodayPrediction == "Rainy":
            TransCondition = np.random.choice(TransitionStates[1], replace=True, p=TransitionMatrix[1])
            if TransCondition == "RaRa":
                pass
            else:
                TodayPrediction = "Sunny"

        WeatherForecasting.append(TodayPrediction)
        print(TodayPrediction)
    return WeatherForecasting


def plot_weather(WeatherForecasting):
    plt.figure()
    plt.plot(WeatherForecasting)
    plt.show()


def plot_weather_hist(WeatherForecasting):
    plt.figure()
    plt.hist(WeatherForecasting)
    plt.show()


if __name__ == "__main__":
    forecast = weather()
    plot_weather(forecast)
    plot_weather_hist(forecast)
