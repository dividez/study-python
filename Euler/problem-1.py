# -*- coding: utf-8 -*-
__author__ = 'Jim'
'''
Problem 1 https://projecteuler.net/problem=1
'''
total = 0
for i in range(1000):
    if ((i % 3 == 0) or (i % 5 == 0)):
       total += i

print(total)