# -*- coding: utf-8 -*-
# @Time    : 2020/1/23 23:15
# @Author  : -- CXS --
# @File    : 桶排序.py


def bucketSort(argList):
    '''
    将多个数平均放置在多个桶中，
    每个桶进行排序
    :param argList:
    :return:
    '''
    minValue = min(argList)
    maxValue = max(argList)
    # 确定桶的大小
    bucketSize = (maxValue - minValue) / len(argList)
    # 初始化桶数组
    bucketList = [[] for i in range(len(argList) + 1)]
    # 向桶中平均地填入数
    for i in argList:
        bucketList[int((i - minValue))//bucketSize].append(i)
    argList.clear()
    # 每个桶排序，回填到argList
    for i in bucketList:
        for j in sorted(i):
            argList.append(j)


