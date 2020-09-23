# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/23  10:26 上午
"""


def findnode(root, node1, node2):
    if root == None or root == node1 or root == node2:
        return root
    lchild = findnode(root.lchild, node1, node2)
    rchild = findnode(root.rchild, node1, node2)
    if lchild == None:
        return rchild
    elif rchild == None:
        return lchild
    else:
        return root


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def arraytotree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start + end + 1) // 2
        root.data = arr[mid]
        root.lchild = arraytotree(arr, start, mid - 1)
        root.rchild = arraytotree(arr, mid + 1, end)
    else:
        root = None
    return root


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arraytotree(arr, 0, len(arr) - 1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.lchild
    res = None
    res = findnode(root, node1, node2)
    if res != None:
        print('最近的节点为：' + str(res.data))
    else:
        print('没有父节点')
