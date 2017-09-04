# -*- coding: utf-8 -*-
__author__ = 'Jim'

# 和 map() 类似， filter() 也接收一个函数和一个序列。
# 和 map() 不同的时，filter() 把传入的函数依次作用于每个元素
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 用filter()删除1~100的素数

import math


def prime(n):
    if n == 1:
        return True
    for i in range(2, 10):
        if i != n and n % i == 0:
            return False
        else:
            continue
    return True


list = range(1, 100)
print filter(prime, list)
