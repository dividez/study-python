# -*- coding: utf-8 -*-
__author__ = 'Jim'
'''
Problem 2 https://projecteuler.net/problem=2
'''

a = [1, 2]
total = 2
i = 2
while (1):
    next = a[i - 1] + a[i - 2]
    a.append(next)
    if next % 2 == 0:
        total = total + next
    if next > 4000000:
        break
    i += 1

print(total)
