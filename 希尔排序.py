# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:57
# @Author  : -- CXS --
# @File    : 希尔排序.py

def shellSort(arg_list):
    # 希尔排序，即递减增量排序算法
    # 是插入排序的一种更高效的改进版本
    # 思路：分组插入排序 -> 增量减半 -> ... -> 整体插入排序
    # 适用于大规模无序数列
    import math
    increment = 1  # 增量
    while (increment < len(arg_list) / 2):
        increment = increment * 2 + 1
    while increment > 0:
        for i in range(increment, len(arg_list)):
            preIndex = i - increment
            currentNum = arg_list[i]
            while preIndex >= 0 and arg_list[preIndex] > currentNum:
                arg_list[preIndex + increment] = arg_list[preIndex]
                preIndex -= increment
            arg_list[preIndex + increment] = currentNum
        increment = math.floor(increment / 2)
    return arg_list
