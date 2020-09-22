class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def createSingleLink():
    head = Node(1)
    cur = head
    for i in range(2, 10):
        cur.next = Node(i)
        cur = cur.next
    return head

def printSingleLink(head):
    cur = head
    while cur is not None:
        print(cur.data, end='')
        if cur.next is not None:
            print("-->", end='')
        cur = cur.next
    print(' ')
    return None

def Reverse(head):
    pre = None
    cur = head
    while cur is not None:
        next_ = cur.next
        cur.next = pre
        pre = cur
        cur = next_
    return pre

if __name__ == '__main__':
    singleHead = createSingleLink()
    printSingleLink(singleHead)
    reverSingleHead = Reverse(singleHead)
    printSingleLink(reverSingleHead)