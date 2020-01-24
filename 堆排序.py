# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 13:44
# @Author  : -- CXS --
# @File    : 堆排序.py
from generate_random_nums import GenerateRandomNum

def headSort(argList):
    """
    堆排序
    利用完全二叉树原理实现
    暂时只掌握原理
    :param argList:
    :return:
    """
    global arrLen
    arrLen = len(argList)
    buildMaxHeap(argList)
    for i in range(len(argList)-1,0,-1):
        swap(argList,0,i)
        arrLen -= 1
        heapify(argList,0)
    return argList

def heapify(argList,i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arrLen and argList[left] > argList[largest]:
        largest = left
    if right < arrLen and argList[right] > argList[largest]:
        largest = right
    if largest != i:
        swap(argList,i,largest)
        heapify(argList,largest)

def swap(argList,i,j):
    argList[i],argList[j] = argList[j],argList[i]

def buildMaxHeap(argList):
    import math
    for i in range(math.floor(len(argList)/2),-1,-1):
        heapify(argList,i)

gen = GenerateRandomNum()
i = gen.int_list(100,1,1000)
f = gen.float_list(100,1,1000)
print(headSort(i))
print(headSort(f))
