# -*- coding: utf-8 -*-
__author__ = 'Jim'

# KMP

def KMP_index(ori, par):
    slen = len(ori)
    tlen = len(par)
    if slen >= tlen:
        ii = 0
        jj = 0
        next_list = [-2 for i in range(len(par))]
        next_arr(par, next_list)
        print next_list
        while ii < slen:
            if jj == -1 or ori[ii] == par[jj]:
                ii = ii + 1
                jj = jj + 1
            else:
                jj = next_list[jj]
            if jj == tlen:
                return ii - tlen
    return -1


def next_arr(t, next_array):
    next_array[0] = -1
    i = 0
    j = -1
    while i < len(t) - 1:
        if j == -1 or t[i] == t[j]:
            i = i + 1
            j = j + 1
            if t[i] != t[j]:
                next_array[i] = j
            else:
                next_array[i] = next_array[j]
        else:
            j = next_array[j]

    return next_array


def main():
    ori = "BBC ABCDABD ABCD E"  # 原串
    par = "ABCDABD"  # 模式串
    print KMP_index(ori, par)


main()
