# 输入一个链表，输出链表中倒数第k个节点
# 设一个快指针，一个慢指针，快指针先往前走(k-1)步。然后快慢指针分别向前一步，当快指针到达末尾时，慢指针刚好到达倒数第k个。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_to_tail(pHead, k):
    if not pHead:
        return None
    slow = pHead
    fast = pHead

    # 快指针先往前 k-1步
    for i in range(1, k):
        # 如果k超出了链表长度，返回None
        if not fast.next:
            return None
        fast = fast.next

    # 快指针和慢指针依次向前，直到快指针到达终点，返回慢指针所在节点
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.val

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

find_kth_to_tail(head,4)