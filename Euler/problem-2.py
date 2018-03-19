# -*- coding: utf-8 -*-
__author__ = 'Jim'
'''
Problem 2 https://projecteuler.net/problem=2
'''
a, b = 1, 2
limit = 4000000
sumTotal = 0
while a < limit:
    a, b = b, a + b
    sumTotal += a if a % 2 == 0 else 0

print(sumTotal)