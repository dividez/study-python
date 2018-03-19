# -*- coding: utf-8 -*-
from math import sqrt

__author__ = 'Jim'

'''
problem 3 https://projecteuler.net/problem=3

求区 MAX 的素约数
'''

MAX = 600851475143


def primeFactor(n):
    a = []
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            a.append(i)
            n = n / i
    print(a)


primeFactor(MAX)
