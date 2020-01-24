# -*- coding: utf-8 -*-
# @Time    : 2020/1/23 22:47
# @Author  : -- CXS --
# @File    : 计数排序.py
from generate_random_nums import GenerateRandomNum

def countingSort(arg_list,maxValue):
    '''
    排序时间最少
    无法排序浮点数
    :param arg_list:
    :param maxValue:
    :return:
    '''
    bucketLen = maxValue + 1  # 新开辟一个桶序列来计数
    bucket = [0] * bucketLen  # 初始化桶序列
    sortedIndex = 0  # 从桶中取出后的排序指针
    arrLen = len(arg_list)
    for i in range(arrLen):
        # 用桶序列来计数
        bucket[arg_list[i]] += 1
    for j in range(bucketLen):
        # 重置arg_list
        while bucket[j]:
            arg_list[sortedIndex] = j
            bucket[j] -= 1
            sortedIndex += 1
    return arg_list

gen = GenerateRandomNum()
i = gen.int_list(100,1,1000)
f = gen.float_list(100,1,1000)
print(countingSort(i,max(i)))
print(countingSort(f,max(f)))



