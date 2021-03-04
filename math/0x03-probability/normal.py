#!/usr/bin/env python3
"""Normal"""


class Normal:
    """Normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            self.mean = mean
            self.stddev = stddev
        else:
            self.data = data
            self.mean = StatFuncs.avg(self.data)
            self.stddev = StatFuncs.stddev(self.data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != list:
            raise TypeError('data must be a list')
        elif len(value) < 1:
            raise ValueError('data must contain values')
        self.__data = value

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, value):
        self.__mean = float(value)

    @property
    def stddev(self):
        return self.__stddev

    @stddev.setter
    def stddev(self, value):
        if value <= 0:
            raise ValueError('stddev must be a positive value')
        self.__stddev = float(value)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return (self.stddev * z) + self.mean

    def pdf(self, x):
        """Probability Density Function"""
        factor = 1 / (self.stddev * (2 * MathSymbols.pi) ** 0.5)
        exponent = (-0.5) * (self.z_score(x) ** 2)
        return factor * (MathSymbols.e ** exponent)

    def cdf(self, x):
        """Cummulative density function"""
        error_param = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return 0.5 * (1 + StatFuncs.errfunc(error_param))


class MathSymbols:
    """Math symbols used in calculations"""
    e = 2.7182818285
    pi = 3.1415926536


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
    def errfunc(x):
        """Aprox. Error function"""
        denoms = (1, -3, 10, -42, 216)
        exps = (1, 3, 5, 7, 9)
        x_s = [x] * len(exps)
        serie = map(lambda k, expn, den: (k ** expn) / den, x_s, exps, denoms)
        return (2 / (MathSymbols.pi ** 0.5)) * sum(serie)
