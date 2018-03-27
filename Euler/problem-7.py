# -*- coding: utf-8 -*-
from math import sqrt

__author__ = 'Jim'

'''
Problem 7 https://projecteuler.net/problem=7

'''


def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


the_10001st = 0
for i in range(2, 10 ** 9):

    the_10001st += isprime(i)
    if the_10001st == 10001:
        print(i)
        break
