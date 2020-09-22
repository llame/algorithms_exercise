
'''
给定链表L0 -> L1 -> L2 -> … -> Ln-1 -> Ln ，
把链表重新排序为 L0 -> Ln -> L1 -> Ln-1 -> L2 … 。
要求：（1）在原来链表的基础上进行排序，即不能申请新的结点；
（2）只能修改结点的next域，不能修改数据域。
'''

# 双路归并函数merge()先是定义了一个虚拟的头节点，来做为排序链表的头节点；
# 指针p记录归并后的排序链表的最后一个元素，
# 每次从左右(left、right)链表中取最小的元素，放在p指针上，
# 此时p指针下移，被取元素的链表，指针同样下移，
# 没被取元素的链表不用动。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # step1:寻找中心点，划分左右区域
        def findMid(head):
            slow = head
            fast = head
            # 快慢指针的这个判断条件要注意
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        # step2:有序链表的双路归并
        def merge(l,r):
            dummy = ListNode(None)
            p = dummy
            while l and r:
                if l.val <= r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            p.next = l or r
            return dummy.next

        # step3:归并排序的主程序
        if not head or not head.next:
            return head

        mid = findMid(head)

        left = head
        right = mid.next
        mid.next = None

        l = self.sortList(left)
        r = self.sortList(right)

        return merge(l,r)


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


list_val = [0, -1, 2, 3, -3, 9]
head=get_listnode_by_list(list_val)
result=Solution().sortList(head)



