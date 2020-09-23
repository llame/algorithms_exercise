# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/23  4:10 下午
"""


def min_distance(arr, num1, num2):
    if (num1 not in arr) or (num2 not in arr):
        return -1

    mindis = 2 ** 32
    i = 0
    pos1 = -1
    pos2 = -1
    while i < len(arr):
        if arr[i] == num1:
            pos1 = i
            if pos2 > 0:
                dist = abs(pos1 - pos2)
                mindis = min(dist, mindis)
        if arr[i] == num2:
            pos2 = i
            if pos1 > 0:
                dist = abs(pos1 - pos2)
                mindis = min(dist, mindis)
        i += 1
    return mindis


if __name__ == '__main__':
    list_array = [4, 5, 6, 4, 7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8]
    num1 = 4
    num2 = 7
    result=min_distance(list_array,num1,num2)
    print('min distance:',result)
