# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 17:12
# @Author  : -- CXS --
# @File    : 冒泡排序(bubble-sort).py

from generate_random_nums import GenerateRandomNum
from datetime import datetime

class SortingAlgorithm():
    '''
    python实现十种经典排序算法
    '''

    @classmethod
    def bubbleSort(cls,arg_list):
        # 冒泡排序
        for i in range(1,len(arg_list)):
            for j in range(0,len(arg_list)-i):
                if arg_list[j] > arg_list[j+1]:
                    arg_list[j],arg_list[j+1] = arg_list[j+1],arg_list[j]
        return arg_list

    @classmethod
    def selectionSort(cls,arg_list):
        # 选择排序
        # 无论什么数据都是O(n^2)的时间复杂度，适用于数据规模较小的情况
        for i in range(len(arg_list)):
            minIndex = i
            for j in range(i+1,len(arg_list)):
                if arg_list[j] < arg_list[minIndex]:
                    minIndex = j
            if i != minIndex:
                arg_list[i],arg_list[minIndex] = arg_list[minIndex],arg_list[i]
        return arg_list

    @classmethod
    def InsertSort(cls,arg_list):
        # 插入排序
        # 适用于小规模数据或基本有序数列
        for i in range(1,len(arg_list)):
            preIndex = i-1
            currentNum = arg_list[i]
            while preIndex >= 0 and arg_list[preIndex] > currentNum:
                arg_list[preIndex+1] = arg_list[preIndex]
                preIndex -= 1
            arg_list[preIndex + 1] = currentNum
        return arg_list

    @classmethod
    def shellSort(cls,arg_list):
        # 希尔排序，即递减增量排序算法
        # 是插入排序的一种更高效的改进版本
        # 思路：分组插入排序 -> 增量减半 -> ... -> 整体插入排序
        # 适用于大规模无序数列
        import math
        increment = 1  # 增量
        while (increment < len(arg_list)/2):
            increment = increment * 2 + 1
        while increment > 0:
            for i in range(increment, len(arg_list)):
                preIndex = i - increment
                currentNum = arg_list[i]
                while preIndex >= 0 and arg_list[preIndex] > currentNum:
                    arg_list[preIndex + increment] = arg_list[preIndex]
                    preIndex -= increment
                arg_list[preIndex + increment] = currentNum
            increment = math.floor(increment/2)
        return arg_list

    @classmethod
    def mergeSort(cls,arg_list):
        # 归并排序,分而治之
        import math
        if len(arg_list) < 2:
            return arg_list
        middle = math.floor(len(arg_list)/2)
        left,right = arg_list[:middle],arg_list[middle:]
        return cls.mergeResult(cls.mergeSort(left),cls.mergeSort(right))
    @classmethod
    def mergeResult(cls,left_part,right_part):
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

    @classmethod  # 有bug，待解决
    def quickSort(cls,arg_list,left = None,right = None): # 后面要用到，先定义为None
        # 快速排序
        # 效率高，处理大数据最快的排序算法
        left = 0 if not left else left  # 左指针
        right = (len(arg_list)-1) if not right else right  # 右指针
        if left < right:  # 左右指针相等时停止递归
            markIndex = cls.partition(arg_list,left,right)  # 确定基准指针位置
            cls.quickSort(arg_list,left,markIndex-1)  # 左半部递归
            cls.quickSort(arg_list,markIndex+1,right)  # 右半部递归
        return arg_list
    @classmethod
    def partition(cls,arg_list,left,right):
        pivot = left  # 以左边第一个数为基准
        index = pivot + 1  # 从第二个数开始遍历
        i = index  # 用于遍历的指针
        while i <= right:
            if arg_list[i] < arg_list[pivot]:  # 把小于基准的放在指针左边
                cls.swap(arg_list,i,index)
                index += 1
            i += 1  # 遍历整个列表
        cls.swap(arg_list,pivot,index-1)
        return index-1
    @classmethod
    def swap(cls,arg_list,i,j):
        arg_list[i],arg_list[j] = arg_list[j],arg_list[i]

    def headSort(self,arg_list):
        # 堆排序
        global arrLen
        arrLen = len(arg_list)
        buildMaxHeap(arg_list)

    @classmethod
    def countingSort(cls,arg_list):
        pass








if __name__ == '__main__':
    gen = GenerateRandomNum()
    i = gen.int_list(100,1,1000)
    f = gen.float_list(100,1,1000)
    # end_time = datetime.now()
    # print(f, '\n', i)
    # print(SortingAlgorithm.bubbleSort(f), '\n', SortingAlgorithm.bubbleSort(i))
    # print(SortingAlgorithm.selectionSort(f), '\n', SortingAlgorithm.selectionSort(i))
    # print(SortingAlgorithm.InsertSort(f), '\n', SortingAlgorithm.InsertSort(i))
    # print(SortingAlgorithm.shellSort(f), '\n', SortingAlgorithm.shellSort(i))
    start_time = datetime.now()
    print(SortingAlgorithm.mergeSort(f), '\n', SortingAlgorithm.mergeSort(i))
    end_time = datetime.now()
    print('归并排序时间：',end_time - start_time)
    start_time2 = datetime.now()
    print(SortingAlgorithm.quickSort(f), '\n', SortingAlgorithm.quickSort(i))
    end_time2 = datetime.now()
    print('快速排序时间：',end_time2 - start_time2)




