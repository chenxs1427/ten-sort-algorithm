# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:56
# @Author  : -- CXS --
# @File    : 冒泡排序.py


def bubbleSort(arg_list):
    # 冒泡排序
    for i in range(1, len(arg_list)):
        for j in range(0, len(arg_list) - i):
            if arg_list[j] > arg_list[j + 1]:
                arg_list[j], arg_list[j + 1] = arg_list[j + 1], arg_list[j]
    return arg_list