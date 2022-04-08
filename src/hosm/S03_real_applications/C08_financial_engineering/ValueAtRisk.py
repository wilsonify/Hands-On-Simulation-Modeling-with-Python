"""
Studying risk models for portfolio management

Having a good risk measure is of fundamental importance in finance,
as it is one of the main tools for evaluating financial assets.
This is because it allows you to monitor securities and provides a criterion for the construction of portfolios.

One measure, more than any other, that has been widely used over the years is variance.

Using variance as a risk measure

The advantage of a diversified portfolio in terms of risk and
the expected value allows us to find the right allocation for the securities.

Our aim is to obtain the highest expected value
at the same risk or to minimize the risk of obtaining the same expected value.

To achieve this, it is necessary to trace the concept of risk back to a measurable quantity,
which is generally referred to as the variance.

Therefore, by maximizing the expected value of the portfolio returns for each level of variance,
it is possible to reconstruct a curve called the efficient frontier,
which determines the maximum expected value that can be obtained
with the securities available for the construction of the portfolio for each level of risk.

The minimum variance portfolio represents the portfolio with the lowest possible variance
value regardless of the expected value.

This parameter has the purpose of optimizing the risk represented by the variance of the portfolio.

Tracing the risk exclusively to the measure of variance is optimal only if the distribution of returns is normal.

In fact, the normal distribution enjoys some properties that make the
variance a measure that is enough to represent the risk.

It is completely determinable through only two parameters (mean and variance).

It is, therefore, enough to know the mean and the variance to determine any other point of the distribution.

Introducing the value-at-risk metric Consider
the variance as the only risk measure in the case of non-normal and limiting values.

A risk measure that has been widely used for over two decades is Value at Risk (VaR).

The birth of VaR was linked to the growing need for financial institutions to manage risk and,
therefore, be able to measure it.

This is due to the increasingly complex structure of financial markets.

Actually, this measure was not introduced to stem the limits of variance as a
risk measure since an approach to calculate the VaR value starts precisely from the assumptions of normality.

However, to make it easier to understand,
let's enclose the overall risk of a security into a
single number or a portfolio of financial assets by adopting a single metric for different types of risk.

In the financial context, the VaR is an estimate,
given a confidence interval,
of how high the losses of a security or portfolio may be in each time horizon.

The VaR, therefore, focuses on the left tail of the distribution of returns,
where events with a low probability of realization are located.

Indicating the losses and not the dispersion of the returns around their expected value makes it a measure closer to the common idea of risk than variance.222

Important note
J.P. Morgan is credited as the bank that made VaR a widespread measure.
In 1990, the president of J.P. Morgan, Dennis Weatherstone,
was dissatisfied with the lengthy risk analysis reports he received every day.
He wanted a simple report that summarized the bank's total exposure across its entire trading portfolio.

After calculating the VaR, we can say that, with a probability given by the confidence interval,
we will not lose more than the VaR of the portfolio in the next N days.

VaR is the level of loss that will not be exceeded with a probability given by the confidence interval.

For example,
a VaR of €1 million over a year with a 95% confidence level
 means that the maximum loss for the portfolio for the next year will be €1 million in 95% of cases.

Nothing tells us what happens to the remaining 5% of cases.
The following graph shows the probability distribution of portfolio returns
with the indication of the value of the VaR:

VaR is a function of the following two parameters:
• Time horizon
• Level of confidence

Some characteristics of VaR must be specified:
• VaR does not describe the worst loss.
• VaR says nothing about the distribution of losses in the left tail.
• VaR is subject to sampling errors.

Important note
The sampling error tells us how much the sampled value deviates from the real population value.

This deviation is because the sample is not representative of the population or has distortions.

VaR is a widely used risk measure that summarizes, in a single number,
important aspects of the risk of a portfolio of financial instruments.

It has the same unit of measurement as the returns of the portfolio on which it is calculated,
and it is simple to understand, answering the simple question: How bad can financial investments go?

Let's now examine a practical case of calculating the VaR.

Estimating the VaR for some NASDAQ assets

NASDAQ is one of the most famous stock market indices in the world.

Its name is an acronym for the National Association of Securities Dealers Quotation.

This is the index that represents the stocks of the technology sector in the US.

Thinking of NASDAQ in the investor's mind,
the brands of the main technological and social houses of the US can easily emerge.

Just think of companies such as Google, Amazon, Facebook, and many others;
they are all covered by the NASDAQ listing.

Here, we will learn how to recover the data of the quotes of six companies listed by NASDAQ,
and then we will demonstrate how to estimate the risk associated with the
purchase of a portfolio of shares of these securities:
"""
import datetime as dt
import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

StockList = ['ADBE', 'CSCO', 'IBM', 'NVDA', 'MSFT', 'HPQ']


def read_StockClose():
    StartDay = dt.datetime(2019, 1, 1)
    EndDay = dt.datetime(2019, 12, 31)
    StockData = wb.DataReader(StockList, 'yahoo', StartDay, EndDay)
    StockClose = StockData["Adj Close"]
    print(StockClose.describe())
    return StockClose


def value_at_risk(StockClose):
    StockReturns = StockClose.pct_change()
    print(StockReturns.tail(15))
    PortvolioValue = 1000000000.00
    ConfidenceValue = 0.95
    MeanStockRet = np.mean(StockReturns)
    StdStockRet = np.std(StockReturns)
    WorkingDays2019 = 252.
    AnnualizedMeanStockRet = MeanStockRet / WorkingDays2019
    AnnualizedStdStockRet = StdStockRet / np.sqrt(WorkingDays2019)

    INPD = norm.ppf(1 - ConfidenceValue, AnnualizedMeanStockRet, AnnualizedStdStockRet)
    VaR = PortvolioValue * INPD

    RoundVaR = np.round_(VaR, 2)

    for i in range(len(StockList)):
        print("Value-at-Risk for", StockList[i], "is equal to ", RoundVaR[i])


def plot_StockClose(StockClose):
    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(StockClose['ADBE'])
    axs[0, 0].set_title('ADBE')
    axs[0, 1].plot(StockClose['CSCO'])
    axs[0, 1].set_title('CSCO')
    axs[1, 0].plot(StockClose['IBM'])
    axs[1, 0].set_title('IBM')
    axs[1, 1].plot(StockClose['NVDA'])
    axs[1, 1].set_title('NVDA')
    axs[2, 0].plot(StockClose['MSFT'])
    axs[2, 0].set_title('MSFT')
    axs[2, 1].plot(StockClose['HPQ'])
    axs[2, 1].set_title('HPQ')

    plt.figure(figsize=(10, 5))
    plt.plot(StockClose)
    plt.show()


if __name__ == "__main__":
    stock_close = read_StockClose()
    plot_StockClose(stock_close)
    value_at_risk(stock_close)
