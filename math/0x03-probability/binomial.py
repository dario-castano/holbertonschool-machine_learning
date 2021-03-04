#!/usr/bin/env python3
"""Binomial"""


class Binomial:
    """Binomial Distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            self.n = n
            self.p = p
        else:
            self.data = data
            self.n, self.p = self.__npbuild()

    def __npbuild(self):
        """Build n and p using data"""
        mu = StatFuncs.avg(self.data)
        variance = StatFuncs.stddev(self.data) ** 2
        n = round(mu / (1 - (variance / mu)))
        p = mu / n
        return n, p

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != list:
            raise TypeError('data must be a list')
        elif len(value) <= 2:
            raise ValueError('data must contain multiple values')
        self.__data = value

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, value):
        if value <= 0 or value >= 1:
            raise ValueError('p must be greater than 0 and less than 1')
        self.__p = float(value)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if value <= 0:
            raise ValueError('n must be a positive value')
        self.__n = int(value)

    def pmf(self, k):
        """Probability Mass Function"""
        if k < 0:
            return 0
        x = int(k)
        combi = StatFuncs.combination(self.n, x)
        succ = self.p ** x
        fail = (1 - self.p) ** (self.n - x)
        return combi * succ * fail

    def cdf(self, k):
        """Cummulative density function"""
        if k < 0:
            return 0
        x = int(k)
        indexes = range(x + 1)
        probs = map(self.pmf, indexes)
        return sum(probs)


class StatFuncs:
    """Some statistical functions"""
    @staticmethod
    def factorial(n, acc=1):
        """Factorial of a number"""
        if n < 0:
            raise ValueError('parameter must be greater than 0')
        elif n == 0:
            return acc
        else:
            return StatFuncs.factorial(n-1, n*acc)

    @staticmethod
    def avg(data):
        """Average of a list"""
        if type(data) != list:
            raise TypeError('parameter must be a list')
        elif len(data) < 1:
            raise ValueError('list should have 1 or more elements')
        return sum(data) / len(data)

    @staticmethod
    def stddev(data):
        """Standard deviation"""
        if type(data) != list:
            raise TypeError('parameter must be a list')
        elif len(data) < 1:
            raise ValueError('list should have 1 or more elements')
        else:
            means = [StatFuncs.avg(data)] * len(data)
            devs = map(lambda x, mu:  (x - mu) ** 2, data, means)
            return (sum(devs) / len(data)) ** 0.5

    @staticmethod
    def combination(n, r):
        """Calculates a combination"""
        f_n = StatFuncs.factorial(n)
        f_r = StatFuncs.factorial(r)
        f_nr = StatFuncs.factorial(n - r)
        return f_n / (f_r * f_nr)
