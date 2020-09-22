# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  10:13 上午
"""


class Node(object):
    '''
    define node
    '''

    def __init__(self, val, next=None):
        self.val = val  # 对应元素值
        self.next = next  # 表示下一个链接的链点


class Queue(object):
    '''定义队列'''

    def __init__(self):
        self.head = None  # 头部链点为 None
        self.rear = None  # 尾部链点为 None

    def is_empty(self):  # 判断队列是否为空
        return self.head is None  # 判断队列是否为空

    def enqueue(self, val):  # 进入队列
        new_node = Node(val)  # 构建新的节点
        if self.is_empty():
            self.head = new_node  # 队列头部为新的链点
            self.rear = new_node  # 队列尾部为新的链点
        else:
            self.rear.next = new_node  # 队列尾部的元素指向下一个后继
            self.rear = new_node  # 队列指针指向下一个节点

    def dequeue(self):  # 出队列
        if self.is_empty():  # 如果为空，则打印空
            print('queue is empty')
        else:
            result = self.head.val  # 非空，则返回队列头部元素
            self.head = self.head.next  # 指针指向下一个元素
            return result

    def peek(self):  # 获取头部元素
        if self.is_empty():  # 如果为空，则打印空
            print('queue is empty')
        else:  # 否则输出队列头部元素对应的值
            return self.head.val

    def print_queue(self):
        print('queue')
        tmp = self.head  # 临时指针
        myqueue = []  # 列表存储队列元素
        while tmp is not None:
            myqueue.append(tmp.val)
            tmp = tmp.next
        print(myqueue)

if __name__ == '__main__':
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.peek()
    queue.print_queue()
    queue.is_empty()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()


