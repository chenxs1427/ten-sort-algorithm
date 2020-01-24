# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:59
# @Author  : -- CXS --
# @File    : 快速排序.py

def quickSort(arg_list, left=None, right=None):  # 后面要用到，先定义为None
    # 快速排序
    # 效率高，处理大数据最快的排序算法
    left = 0 if not left else left  # 左指针
    right = (len(arg_list) - 1) if not right else right  # 右指针
    if left < right:  # 左右指针相等时停止递归
        markIndex = partition(arg_list, left, right)  # 确定基准指针位置
        quickSort(arg_list, left, markIndex - 1)  # 左半部递归
        quickSort(arg_list, markIndex + 1, right)  # 右半部递归
    return arg_list

def partition(arg_list, left, right):
    pivot = left  # 以左边第一个数为基准
    index = pivot + 1  # 从第二个数开始遍历
    i = index  # 用于遍历的指针
    while i <= right:
        if arg_list[i] < arg_list[pivot]:  # 把小于基准的放在指针左边
            swap(arg_list, i, index)
            index += 1
        i += 1  # 遍历整个列表
    swap(arg_list, pivot, index - 1)
    return index - 1

def swap(arg_list, i, j):
    arg_list[i], arg_list[j] = arg_list[j], arg_list[i]
