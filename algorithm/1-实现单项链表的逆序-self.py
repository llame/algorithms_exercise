class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

def create_single_link(node_number):
    '''
    创建单向链表
    :param node_number:节点数
    :return: head 第一个节点
    '''
    print('创建链表,节点个数{node_number}'.format(node_number=node_number))
    head=Node(1)
    cur=head
    for i in range(2,node_number+1):
        tmp=Node(i)
        cur.next=tmp
        cur=cur.next
    return head


def print_single_link(head):
    '''
    打印链表
    :param head:
    :return:
    '''
    data_list=[]
    cur=head
    while(cur is not None):
        data_list.append(cur.data)
        cur = cur.next
    data_list=[str(i) for i in data_list]
    print('-->'.join(data_list))
    return None


def reverse_link(head):
    '''
    反转链表
    :param head:
    :return:
    '''
    pre=None
    cur=head
    while(cur is not None):
        next_node=cur.next
        cur.next=pre

        pre=cur
        cur=next_node

    return pre

if __name__ == '__main__':
    node_number=10
    head=create_single_link(node_number)
    print_single_link(head)

    print('反转链表')
    head=reverse_link(head)
    print_single_link(head)


