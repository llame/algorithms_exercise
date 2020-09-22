# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/21  5:42 下午
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def con_link(n):
    head = Node()
    cur = head
    for i in range(1, n + 1):
        node = Node(i)
        cur.next = node
        cur = node
    return head


def print_link(head):
    if head is None or head.next is None:
        return
    cur = head.next
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()

def reverseKNode(head, k):
    if head is None or head.next is None:
        return
    if k == 0 or k == 1:
        return head
    pre = head
    begin = head.next
    while begin:
        end = begin
        for i in range(k-1):
            if end.next:
                end = end.next
            else:
                return head
        next= end.next
        end.next = None
        r_head, r_end = reverseLink(begin)
        r_end.next = next
        pre.next = r_head
        pre = r_end
        begin = next
    return head




def reverseLink(head):
    if head is None or head.next is None:
        return
    r_end = head
    pre = head
    r_head = pre.next
    pre.next = None
    while r_head.next:
        next = r_head.next
        r_head.next = pre
        pre = r_head
        r_head = next
    r_head.next = pre
    return r_head, r_end


if __name__ == '__main__':
    n = int(input("请输入n："))
    k = int(input("请输入k："))
    head = con_link(n)
    print_link(head)
    head = reverseKNode(head, k)
    print_link(head)