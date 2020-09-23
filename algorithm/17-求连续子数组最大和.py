# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/23  3:55 下午
"""


def cal_max_sum_subarry(list_array):
    '''
    :param list_array:
    :return:
    '''
    max_sum = 0
    pre_array_sum = 0
    for i in list_array:
        if pre_array_sum <= 0:  # 如果之前只和小于0，那么最大子数组一定不含之前的数组
            pre_array_sum = i
        else:
            pre_array_sum = pre_array_sum + i  # 加上当前元素值并与目前维护的最大值进行比较

        if pre_array_sum > max_sum:
            max_sum = pre_array_sum
    return max_sum


if __name__ == '__main__':
    list_ini = [1, 2, -1, -3, 6, 6, -4, 5, 2, 3, 6, -9, 10]
    max_sum = cal_max_sum_subarry(list_ini)
