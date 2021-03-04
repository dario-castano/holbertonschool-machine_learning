#!/usr/bin/env python3
"""Exponential"""


class Exponential:
    """Exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            self.lambtha = lambtha
        else:
            self.data = data
            self.lambtha = StatFuncs.inv_avg(data)

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

    def pdf(self, x):
        """Probability Density Function"""
        if x < 0:
            return 0
        exp_inv_lambdax = 1 / (MathSymbols.e ** (self.lambtha * x))
        return self.lambtha * exp_inv_lambdax

    def cdf(self, x):
        """Cummulative density function"""
        if x < 0:
            return 0
        exp_inv_lambdax = 1 / (MathSymbols.e ** (self.lambtha * x))
        return 1 - exp_inv_lambdax


class MathSymbols:
    """Math symbols used in calculations"""
    e = 2.7182818285


class StatFuncs:
    """Some statistical functions"""
    @staticmethod
    def inv_avg(data):
        """Inverse Average of a list"""
        if type(data) != list:
            raise TypeError('parameter must be a list')
        elif len(data) < 1:
            raise ValueError('list should have 1 or more elements')
        return 1 / (sum(data) / len(data))
