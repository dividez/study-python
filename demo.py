# -*- coding: utf-8 -*-
#
def prod(s):
    def get_s(x, y):
        return x * y

    return reduce(get_s, s)


ls = [2, 3, 5, 8]

print prod(ls)
