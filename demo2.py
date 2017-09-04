# -*- coding: utf-8 -*-
# map()函数接收两个参数，一个是函数，
# 一个是序列，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的list返回。




str_l = ['adam', 'LISA', 'barT']


def str_to_up_f(str):
    return str.capitalize()


temp = map(str_to_up_f, str_l)

print  temp

