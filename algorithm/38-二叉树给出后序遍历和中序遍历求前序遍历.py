# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/10/16  3:01 下午
"""
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution():
    def reConstructBinaryTree(self,ldr,lrd):
        '''
        :param LDR: 中序遍历
        :param LRD: 后序遍历
        :return:
        '''
        if len(ldr)==0:
            return None
        root=TreeNode(lrd[-1])
        ldr_index=ldr.index(lrd[-1])

        root.left=self.reConstructBinaryTree(ldr[0:ldr_index],lrd[0:ldr_index])
        root.right=self.reConstructBinaryTree(ldr[ldr_index+1:],lrd[ldr_index:len(lrd)-1])
        return root

    def dlr_print(self,root):
        if root is not None:
            print(root.val)
            self.dlr_print(root.left)
            self.dlr_print(root.right)

if __name__ == '__main__':
    ldr=[4,7,2,1,5,3,8,6]
    lrd=[7,4,2,5,8,6,3,1]
    s=Solution()
    root=s.reConstructBinaryTree(ldr,lrd)
    s.dlr_print(root)


