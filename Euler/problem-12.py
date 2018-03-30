# -*- coding: utf-8 -*-
__author__ = 'Jim'

import operator
import datetime

known = {1: 1}


def getNum(indice):
    if indice in known:
        return known[indice]
    else:
        temp = 0
        temp = getNum(indice - 1) + indice
        known[indice] = temp
        return temp


token = {2: {2: 1}, 3: {3: 1}}


def cnt(num):
    if num in token:
        dvalue = token[num]
    else:
        or_num = num
        dvalue = dict()
        for start in xrange(2, num + 1):
            if not num % start:
                dvalue[start] = 1
                num = num / start
                break
        if num == 1:
            token[or_num] = dvalue
            return dvalue
        dlist = cnt(num)
        for key, value in dlist.iteritems():
            dvalue[key] = dvalue.get(key, 0) + value
        token[or_num] = dvalue

        # print result
    return dvalue


if __name__ == '__main__':
    st = datetime.datetime.now()
    start = 1
    cn = 1
    num = 1
    while cn < 500:
        start += 1
        num = getNum(start)
        # print num,cnt(num)
        cn = reduce(operator.mul, [x + 1 for x in cnt(num).values()])
    print num, start
    en = datetime.datetime.now()
    print en - st
