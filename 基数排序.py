# -*- coding: utf-8 -*-
# @Time    : 2020/1/24 11:06
# @Author  : -- CXS --
# @File    : 基数排序.py

from generate_random_nums import GenerateRandomNum

def radixSort(argList):
    '''
    基数排序
    依次比较个、十位数、百位数...
    有bug
    :param argList:
    :return:
    '''
    i = 0  # 从个位数开始比较
    n = 1  # 最小的位数
    maxValue = max(argList)
    # 确定最大位数
    while maxValue > 10**n:
        n += 1
    while i < n:
        bucket = {}
        for x in range(10):
            bucket.setdefault(x,[])
        # >>> {0:[],1:[],2:[],3:[],...}
        for num in argList:
            radix = int((x / (10**i)) % 10)  # 得到个位数，先将个位数排序，再排十位数...
            bucket[radix].append(num)
        # 重置argList
        j = 0
        for k in range(10):
            # while bucket[k]:
            #     num = bucket[k].pop()
            #     argList[j] = num
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    argList[j] = y
                    j += 1
        i += 1
    return argList

gen = GenerateRandomNum()
i = gen.int_list(100,1,1000)
f = gen.float_list(100,1,1000)
print(radixSort(i))
print(radixSort(f))





