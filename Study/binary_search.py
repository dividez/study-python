# -*- coding: utf-8 -*-
__author__ = 'Jim'


# 自定义函数，实现二分查找，并返回查找结果
def binary_search(find, list1):
    low = 0
    high = len(list1)
    while low <= high:
        mid = (low + high) / 2
        if list1[mid] == find:
            return mid
        # 左半边
        elif list1[mid] > find:
            high = mid - 1
        # 右半边
        else:
            low = mid + 1
    # 未找到返回-1
    return -1


list1 = [1, 2, 3, 7, 8, 9, 10, 5]
# 进行二分查找算法前必须保证要查找的序列时有序的，这里假设是升序列表
list1.sort()

print "原有序列表为:", list1
try:
    find = int(raw_input("请输入要查找的数："))
except:
    print "请输入正整数！"
    exit()

result = binary_search(find, list1)
if result != -1:
    print "要找的元素%d的序号为：%d" % (find, result)
else:
    print "未找到！"
