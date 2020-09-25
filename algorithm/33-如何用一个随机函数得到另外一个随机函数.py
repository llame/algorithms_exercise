# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  3:56 下午
""" 
# 题目描述：有一个函数func1能返回0和1两个值，返回0和1的概率都1/2，
# 问怎么利用这个函数得到另外一个函数func2, 使func2也只能返回0和1，
# 且返回的概率为1/4,返回1的概率为3/4.

import random
def get_random():
    a=int(round(random.random()))
    return a

def get_random_1():
    a=get_random()
    b=get_random()
    if a+b==2:
        return 0
    else:
        return 1

if __name__ == '__main__':
    times=1000000
    zero_number=0

    i=0
    while(i<times):
        tmp=get_random_1()
        if tmp==0:
            zero_number+=1
        i+=1

    print('zero ratio:',zero_number/times)
