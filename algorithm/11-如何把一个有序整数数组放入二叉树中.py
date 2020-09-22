# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  2:59 下午
"""

class BiTNode(object):
    '''
    定义树
    '''
    def __init__(self):
        self.data=None
        self.lchild=None
        self.rchild=None

def array_to_tree(arr,start,end):
    root=None
    if end>=start:#临界条件
        root=BiTNode()
        mid=(start+end+1)//2
        root.data=arr[mid]
        root.lchild=array_to_tree(arr,start,mid-1)
        root.rchild=array_to_tree(arr,mid+1,end)
    else:
        root=None
    return root

def printTreeMidOrder(root):#中序遍历
    if root is None:
        return
    if root.lchild is not None:
        printTreeMidOrder(root.lchild)

    print(root.data)

    if root.rchild is not None:
        printTreeMidOrder(root.rchild)

def printTreeFrontOrder(root):#前序遍历
    if root is None:
        return

    print(root.data)

    if root.lchild is not None:
        printTreeMidOrder(root.lchild)

    if root.rchild is not None:
        printTreeMidOrder(root.rchild)


def printTreeRearOrder(root):  # 后序遍历
    if root is None:
        return

    if root.lchild is not None:
        printTreeMidOrder(root.lchild)

    if root.rchild is not None:
        printTreeMidOrder(root.rchild)

    print(root.data)


if __name__ == '__main__':
    list_example=[1,2,3,4,5,6,7,8,9,10]
    root=array_to_tree(list_example,0,len(list_example)-1)
    print('root:'+str(list_example))

    print('中序遍历输出')
    printTreeMidOrder(root)

    print('前序遍历输出')
    printTreeFrontOrder(root)

    print('后序遍历输出')
    printTreeRearOrder(root)



