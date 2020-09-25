# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  4:18 下午
"""

# 题目描述：随机的从大小为n的数组中选取m个整数，要求每个元素被选中的概率相等。
def get_random(arr,m):
    import random
    length=len(arr)

    i=0
    while(i<m):
        random_int=random.randint(i,length-1)
        tmp=arr[i]
        arr[i]=arr[random_int]
        arr[random_int]=tmp
        i=i+1
    return arr[0:m]

if __name__ == '__main__':
    arr=[1,1,3,4,5,6,7,8,9,10]
    choose=get_random(arr,5)
    print('choose',choose)