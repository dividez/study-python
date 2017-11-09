# -*- coding: utf-8 -*-
__author__ = 'Jim'

N = 12

tag = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def move(x, y, step):
    if step == N:
        return 1
    for i in tag:
        print i


move(1, 1, 1)
