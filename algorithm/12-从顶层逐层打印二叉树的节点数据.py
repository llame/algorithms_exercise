# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  4:16 下午
"""

from collections import deque


class BiTNode:
    def __init__(self):
        self.data = None
        self.fchild = None
        self.rchild = None


def arraytotree(array, start, end):
    """有序数组转换成二叉树"""
    root = None
    if end >= start:
        root = BiTNode()
        mid = int((start + end + 1) / 2)
        # 树的根节点为数组中间的元素
        root.data = array[mid]
        # 递归的用左半部分数组构造root的左子树
        root.lchild = arraytotree(array, start, mid - 1)
        # 递归的用右半部分数组构造root的右子树
        root.rchild = arraytotree(array, mid + 1, end)
    else:
        root = None
    return root


def printTreeLayer(root):
    if root == None:
        return
    queue = deque()
    # 树的根节点进入队列
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        # 访问当前结点
        print(p.data)
        # 如果这个结点的左子树不为空入队列
        if p.lchild != None:
            queue.append(p.lchild)
        if p.rchild != None:
            queue.append(p.rchild)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(array, 0, len(array) - 1)
    print("树的遍历结点为:")
    print(printTreeLayer(root))