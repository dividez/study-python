# -*- coding: utf-8 -*-
__author__ = 'Jim'

'''
Problem 5 https://projecteuler.net/problem=5
最小公倍数

'''


def GYS(m, n):
    if m < n:
        small = m
    else:
        small = n
    for i in range(small, 0, -1):
        if m % i == 0 and n % i == 0:
            return i


def GBS(m, n):
    gongyue = GYS(m, n)
    return (m * n) / gongyue


def getResult(num):
    ans = 1
    for i in range(1, num):
        ans = GBS(int(ans), i)

    return ans


print(getResult(20))
