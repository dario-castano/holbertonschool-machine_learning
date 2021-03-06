#!/usr/bin/env python3
"""Poisson"""


class Poisson:
    """Poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            self.lambtha = lambtha
        else:
            self.data = data
            self.lambtha = StatFuncs.avg(data)

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
    def lambtha(self):
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, value):
        if value <= 0:
            raise ValueError('lambtha must be a positive value')
        self.__lambtha = float(value)

    def pmf(self, k):
        """Probability Mass Function"""
        if k <= 0:
            return 0
        x = int(k)
        lambda_x = self.lambtha ** x
        exp_inv_lambda = 1 / (MathSymbols.e ** self.lambtha)
        x_factorial = StatFuncs.factorial(x)
        result = (lambda_x * exp_inv_lambda) / x_factorial
        return result

    def cdf(self, k):
        """Cummulative density function"""
        if k <= 0:
            return 0

        def lambda_i_fact(i):
            return (self.lambtha ** i) / StatFuncs.factorial(i)

        x = int(k)
        indexes = range(x + 1)
        exp_inv_lambda = 1 / (MathSymbols.e ** self.lambtha)
        summatory = sum(map(lambda_i_fact, indexes))
        return exp_inv_lambda * summatory


class MathSymbols:
    """Math symbols used in calculations"""
    e = 2.7182818285


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
