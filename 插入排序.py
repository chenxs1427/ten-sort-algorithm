# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:57
# @Author  : -- CXS --
# @File    : 插入排序.py

def InsertSort(arg_list):
    # 插入排序
    # 适用于小规模数据或基本有序数列
    for i in range(1, len(arg_list)):
        preIndex = i - 1
        currentNum = arg_list[i]
        while preIndex >= 0 and arg_list[preIndex] > currentNum:
            arg_list[preIndex + 1] = arg_list[preIndex]
            preIndex -= 1
        arg_list[preIndex + 1] = currentNum
    return arg_list
