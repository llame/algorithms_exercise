# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  2:32 下午
"""

# 题目描述：10个房间里放着数量随机的金币，每个房间只能进入一次，并且只能在一个房间中拿金币。
# 一个人采取如下策略：前４个房间只看不拿，随后的房间只要看到比前４个房间都多的金币就拿，
# 否者就拿最后一个房间的金币。编程计算这种策略拿到最多的金币的概率。

import random
def getMaxNum(n):
    if n < 1:
        print("参数不合法")
        return

    a = [None] * n
    # 随机生成n个房间里金币的个数
    i = 0
    while i < n:
        a[i] = random.uniform(1, n)
        i += 1

    max4 = 0
    i = 0
    while i < 4:
        if a[i] > max4:
            max4 = a[i]
        i += 1
    i = 4
    while i < n - 1:
        if a[i] > max4:
            return True
        i += 1
    return False


if __name__ == "__main__":
    monitorCount = 1000 + 0.0
    succes = 0
    i = 0
    while i < monitorCount:
        if getMaxNum(10):
            succes += 1
        i += 1
    print(succes / monitorCount)
