# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  5:25 下午
""" 

# 1.对于每盏灯，当拉动的次数是奇数时，灯就是亮着的，当拉动的次数是偶数时，灯就是关着的。
# 2.每盏灯拉动的次数与它的编号所含的约数的个数有关，它的编号有几个约数，这盏灯就被拉动几次。

def factorIsOdd(a):
    total = 0
    i = 1
    while i <= a:
        if a % i == 0:
            total += 1
        i += 1

    if total % 2 == 1:
        return 1
    else:
        return 0


def totalCount(num, n):
    count = 0
    i = 0
    while i < n:
        if factorIsOdd(num[i]) == 1:
            print("亮着的灯的编号是：" + str(num[i]))
            count += 1
        i += 1
    return count


if __name__ == "__main__":
    num = [None] * 100
    i = 0
    while i < 100:
        num[i] = i + 1
        i += 1
    count = totalCount(num, 100)
    print("最后总共有" + str(count) + "盏灯亮着。")