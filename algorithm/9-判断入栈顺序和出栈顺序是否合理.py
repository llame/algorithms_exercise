# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  11:23 上午
"""

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

# coding:utf-8
# !/bin/python

import sys


def is_pop_order(pushV, popV):
    '''
    :param pushV: 入栈序列顺序
    :param popV: 出栈序列顺序
    :return:
    '''
    if len(pushV) == 0:
        return False
    stack = []
    j = 0
    for i in range(len(pushV)):
        stack.append(pushV[i])
        while j < len(popV) and stack[-1] == popV[j]:
            stack.pop()
            j += 1
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    p_push = sys.stdin.readline().strip()
    p_stack = sys.stdin.readline().strip()
    print(is_pop_order(p_push, p_stack))


if __name__ == '__main__':
    main()
