from trash.preloaded import Node

def push(head, data):
    '''
    >>> push(None, 1).data
    1
    >>> push(None, 1).next
    >>> push(Node(1), 2).data
    2
    >>> push(Node(1), 2).next.data
    1
    '''
    # return Node(data, head)
    node = Node(None)
    node.data = data
    node.next = head
    return node

def build_one_two_three():
    '''
    >>> build_one_two_three().data
    1
    >>> build_one_two_three().next.data
    2
    >>> build_one_two_three().next.next.data
    3
    >>> build_one_two_three().next.next.next
    '''
    node = push(push(push(None, 3), 2), 1)
    return node

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
