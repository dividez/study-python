# -*- coding: utf-8 -*-
__author__ = 'Jim'

'''
Problem 9 https://projecteuler.net/problem=9

'''


def test():
    for i in range(500, 2, -1):
        for j in range(499 - int(i % 2), 1, -1):
            if (1000 - j) * (j + i) == 500000:
                print(i, j, 1000 - i - j)
                print(str(i * j * (1000 - i - j)))
                return


test()
