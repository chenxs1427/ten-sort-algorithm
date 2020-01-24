# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:58
# @Author  : -- CXS --
# @File    : 归并排序.py

def mergeSort(arg_list):
    # 归并排序,分而治之
    import math
    if len(arg_list) < 2:
        return arg_list
    middle = math.floor(len(arg_list) / 2)
    left, right = arg_list[:middle], arg_list[middle:]
    return mergeResult(mergeSort(left),mergeSort(right))

def mergeResult(left_part, right_part):
    result = []
    while left_part and right_part:
        if left_part[0] < right_part[0]:
            result.append(left_part.pop(0))
        else:
            result.append(right_part.pop(0))
    while left_part:
        result.append(left_part.pop(0))
    while right_part:
        result.append(right_part.pop(0))
    return result
