# -*- coding: utf-8 -*-
__author__ = 'Jim'

'''
八皇后问题
'''

import random


# 随机模块

def conflict(state, col):
    # 冲突函数，row为行，col为列
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row - i):  # 重要语句
            return True
    return False


def queens(num=8, state=()):
    # 生成器函数
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def queenprint(solution):
    # 打印函数
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print line(pos)


# for solution in list(queens(8)):
#     print solution

print '  total number is ' + str(len(list(queens())))
print '  one of the range is:\n'
queenprint(random.choice(list(queens())))



