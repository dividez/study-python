# -*- coding: utf-8 -*-
__author__ = 'Jim'

import time


def now():
    print  int(time.time())


print __name__
# 当我们在命令行运行hello模块文件时，
# Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，
# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。
print now.__name__
if __name__ == '__main__':
    now()
