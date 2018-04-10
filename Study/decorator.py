# -*- coding: utf-8 -*-
import functools
import time

__author__ = 'Jim'

# 装饰器用法
'''

https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000#0

'''


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call %s' % func.__name__
        returnValue = func(*args, **kw)
        # print 'call %s():' % func.__name__
        print 'end call %s' % func.__name__
        return returnValue

    return wrapper


@log
def now():
    localtime = time.asctime(time.localtime(time.time()))
    print "本地时间为 :", localtime


now()
