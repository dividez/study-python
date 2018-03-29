# -*- coding: utf-8 -*-
from math import sqrt

__author__ = 'Jim'

def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

allsum = 17

for i in range(9, 2000000, 2):
    if isprime(i):
        allsum += i
    else:
        continue

print allsum
