# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 17:21
# @Author  : -- CXS --
# @File    : 生成随机整数或浮点数.py

import random

class GenerateRandomNum():
    """
    生成随机数列表的工具类
    """
    def int_list(self,number,min,max):
        # 整数随机数列表
        int_nums = [random.randint(min,max) for _ in range(number)]
        return int_nums

    def float_list(self,number,min,max):
        # 两位数浮点数列表
        mutil_float_nums = [random.uniform(min,max) for _ in range(number)]
        float_nums = list(map(lambda x:round(x,2),mutil_float_nums))
        return float_nums

if __name__ == '__main__':
    gen = GenerateRandomNum()
    i = gen.int_list(10,1,100)
    f = gen.float_list(10,1,100)
    print(f,'\n',i)



