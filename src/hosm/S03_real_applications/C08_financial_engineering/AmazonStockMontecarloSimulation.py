"""
Using Simulation Models for Financial Engineering

The explosive entry of systems based on artificial intelligence and
machine learning has opened up new scenarios for the financial sector.

These methods can bring benefits such as user rights protections,  as well as macroeconomic benefits.

Monte Carlo methods find a natural application in finance for the
numerical resolution of pricing and problems in covered call options.

Essentially, these methods consist of simulating a given process or phenomenon using a given mathematical law and
a sufficiently large set of data,
created randomly from distributions that adequately represent real variables.

The idea is that, if an analytical study is not possible,
or adequate experimental sampling is not possible or convenient,
the numerical simulation of the phenomenon is used.

In this chapter, we will look at practical cases of using simulation methods in a financial context.

You will learn how to use Monte Carlo methods to predict stock prices and how to assess the risk associated with a portfolio of sharess.

Exploring the Amazon stock price trend

The stock market provides an opportunity to quickly earn large amounts of money,
that is, in the eyes of an inexperienced user at least.

Exchanges on the stock market can cause large fluctuations in
price attracting the attention of speculators from all over the world.
In order to obtain revenues from investments in the stock market,
it is necessary to have solid knowledge obtained from years of in-depth study of the phenomenon.
In this context, the possibility of having a tool to predict stock market securities represents a need felt by all.

Let's demonstrate how to develop a simulation model of the stock of one of the most famous companies in the world.

Amazon was founded by Jeff Bezos in the 1990s,
and it was one of the first companies in the world to sell products via the internet.

Amazon stock has been listed on the stock exchange since 1997 under the symbol AMZN.

The historical values of AMZN stock can be obtained from various internet sites that have been dealing
with the stock market over the past 10 years.

We will refer to the performance of AMZN stock on the NASDAQ GS stock quote from 2010-04-08 to 2020-04-07.

In order to get the data from 2020-04-07, we need to select 2020-04-08 on the Yahoo website as the end date.

Data can be downloaded in .csv format from the Yahoo Finance website at https://finance.yahoo.com/quote/AMZN/history/ .

The downloaded AMZN.csv file contains a lot of features,
but we will only use two of them, as follows:
• Date: Date of quote
• Close: Close price

this code will lead us to the simulation of a series
 of predicting scenarios of the performance of the Amazon stock price.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters


def read_amzn_from_csv():
    AmznData = pd.read_csv('AMZN.csv', header=0, usecols=['Date', 'Close'], parse_dates=True, index_col='Date')
    print(AmznData.info())
    print(AmznData.head())
    print(AmznData.tail())
    print(AmznData.describe())
    return AmznData


def LogReturns(AmznData):
    AmznDataPctChange = AmznData.pct_change()
    AmznLogReturns = np.log(1 + AmznDataPctChange)
    print(AmznLogReturns.tail(10))
    return AmznLogReturns


def drift(AmznData):
    AmznLogReturns = LogReturns(AmznData)
    MeanLogReturns = np.array(AmznLogReturns.mean())
    VarLogReturns = np.array(AmznLogReturns.var())
    StdevLogReturns = np.array(AmznLogReturns.std())
    Drift = MeanLogReturns - (0.5 * VarLogReturns)
    print("Drift = ", Drift)
    return Drift


def sim_stockprice(AmznData):
    AmznLogReturns = LogReturns(AmznData)
    print(AmznLogReturns.tail(10))

    MeanLogReturns = np.array(AmznLogReturns.mean())
    VarLogReturns = np.array(AmznLogReturns.var())
    StdevLogReturns = np.array(AmznLogReturns.std())
    Drift = MeanLogReturns - (0.5 * VarLogReturns)
    print("Drift = ", Drift)

    NumIntervals = 2518
    Iterations = 20
    np.random.seed(7)
    SBMotion = norm.ppf(np.random.rand(NumIntervals, Iterations))
    DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)
    StartStockPrices = AmznData.iloc[0]
    StockPrice = np.zeros_like(DailyReturns)
    StockPrice[0] = StartStockPrices

    for t in range(1, NumIntervals):
        StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]
    return StockPrice


def amazon_trend(AmznData):
    AmznLogReturns = LogReturns(AmznData)
    print(AmznLogReturns.tail(10))

    MeanLogReturns = np.array(AmznLogReturns.mean())
    VarLogReturns = np.array(AmznLogReturns.var())
    StdevLogReturns = np.array(AmznLogReturns.std())
    Drift = MeanLogReturns - (0.5 * VarLogReturns)
    print("Drift = ", Drift)

    NumIntervals = 2518
    Iterations = 20
    np.random.seed(7)
    SBMotion = norm.ppf(np.random.rand(NumIntervals, Iterations))
    DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)
    StartStockPrices = AmznData.iloc[0]
    StockPrice = np.zeros_like(DailyReturns)
    StockPrice[0] = StartStockPrices

    for t in range(1, NumIntervals):
        StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]

    AMZNTrend = np.array(AmznData.iloc[:, 0:1])
    return AMZNTrend


def plot_AmznData(AmznData):
    register_matplotlib_converters()
    plt.figure(figsize=(10, 5))
    plt.plot(AmznData)
    plt.show()


def plot_AmznLogReturns(AmznLogReturns):
    plt.figure(figsize=(10, 5))
    plt.plot(AmznLogReturns)
    plt.show()


def plot_StockPrice(StockPrice):
    plt.figure(figsize=(10, 5))
    plt.plot(StockPrice)


def plot_AMZNTrend(AMZNTrend):
    plt.plot(AMZNTrend, 'k*')
    plt.show()


if __name__ == "__main__":
    AmznData = read_amzn_from_csv()
    plot_AmznData(AmznData)

    AmznLogReturns = LogReturns(AmznData)
    plot_AmznLogReturns(AmznLogReturns)

    amzn_trend = amazon_trend(AmznData)
    plot_AMZNTrend(amzn_trend)

    sp = sim_stockprice(AmznData)
    plot_StockPrice(sp)
