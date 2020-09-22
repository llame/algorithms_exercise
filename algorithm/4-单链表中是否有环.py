class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return head
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast=fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False


def get_listnode_by_list(list_val):
    '''
    初始化链表
    :param list_val:
    :return:
    '''
    head = ListNode(list_val[0])
    cur = head

    for i in range(1, len(list_val)):
        cur.next = ListNode(list_val[i])
        cur = cur.next
    return head


class Solution1:
    """
    思路分析:
    判断一个单链表是否有环,
    可以用 set 存放每一个 节点, 这样每次 访问后把节点丢到这个集合里面.
    其实 可以遍历这个单链表, 访问过后,
    如果这个节点 不在 set  里面, 把这个节点放入到 set 集合里面.
    如果这个节点在  set 里面 , 说明曾经访问过, 所以这个链表有重新 走到了这个节点, 因此一定有环.

    如果链表都走完了, 把所有的节点都放完了. 还是没有重复的节点, 那说明没有环.

    """

    def hasCycle(self, head):

        mapping = set()

        flag = False

        p = head

        while p:

            if p not in mapping:
                mapping.add(p)
            else:
                flag = True
                break
            p = p.next

        return flag
    

list_val = [0, -1, 2, 3, -3, 9,20]
head=get_listnode_by_list(list_val)

tmp=ListNode(1)

head.next=tmp
head.next.next=ListNode(100)
head.next.next.next=ListNode(99)
head.next.next.next.next=ListNode(98)
head.next.next.next.next.next=ListNode(97)
head.next.next.next.next.next.next=tmp

Solution().hasCycle(head)