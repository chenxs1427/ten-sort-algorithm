# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:56
# @Author  : -- CXS --
# @File    : 选择排序.py

def selectionSort(arg_list):
    # 选择排序
    # 无论什么数据都是O(n^2)的时间复杂度，适用于数据规模较小的情况
    for i in range(len(arg_list)):
        minIndex = i
        for j in range(i + 1, len(arg_list)):
            if arg_list[j] < arg_list[minIndex]:
                minIndex = j
        if i != minIndex:
            arg_list[i], arg_list[minIndex] = arg_list[minIndex], arg_list[i]
    return arg_list
