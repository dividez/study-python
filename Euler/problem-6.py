# -*- coding: utf-8 -*-
__author__ = 'Jim'

'''
Problem 6 https://projecteuler.net/problem=6

'''


def getSum(n):
    return n * (1 + n) / 2


def getMul(n):
    temp = 0
    for i in range(1, n + 1):
        temp = temp + i ** 2
    return temp


print(getSum(100) ** 2 - getMul(100))
