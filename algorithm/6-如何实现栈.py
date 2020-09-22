# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  9:40 上午
"""


class Stack(object):
    '''
    利用list实现栈
    '''

    def __init__(self):
        '''
        初始化
        '''
        self.stack = []

    def push(self, value):
        '''
        进栈
        :param value:
        :return:
        '''
        self.stack.append(value)

    def pop(self):
        '''
        出栈
        :return:
        '''
        if len(self.stack) >= 1:
            self.stack.pop()
        else:
            raise LookupError('stack is empty')

    def is_empty(self):
        '''
        是否为空
        :return:
        '''
        if len(self.stack) == 0:
            return True
        else:
            return False

    def top(self):
        '''
        获取最新元素
        :return:
        '''
        flag_empty = self.is_empty()
        if not flag_empty: return self.stack[-1]

    def size(self):
        '''
        获取元素个数
        :return:
        '''
        return len(self.stack)


if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.size()
    stack.top()
    stack.is_empty()

