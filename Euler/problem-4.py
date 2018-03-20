# -*- coding: utf-8 -*-
__author__ = 'Jim'

'''
Problem 4 https://projecteuler.net/problem=4
回文数

'''


def isHuiWenNumber(num):
    return str(num) == str(num)[::-1]


def find():
    a = []
    for i in range(100, 1000)[::-1]:
        for j in range(100, 1000)[::-1]:
            if isHuiWenNumber(i * j):
                a.append(i * j)

    return max(a)


print(find())
