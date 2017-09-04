# -*- coding: utf-8 -*-
# reduce 把一个函数作用在一个序列[x1, x2, x3...]上
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
def prod(s):
    def get_s(x, y):
        return x * y

    return reduce(get_s, s)


ls = [2, 3, 5, 8]

print prod(ls)
