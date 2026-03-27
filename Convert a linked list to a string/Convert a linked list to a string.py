from trash.preloaded import Node

def stringify(node):
    '''
    >>> stringify(Node(0, Node(1, Node(2, Node(3)))))
    '0 -> 1 -> 2 -> 3 -> None'
    >>> stringify(None)
    'None'
    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    '0 -> 1 -> 4 -> 9 -> 16 -> None'
    '''
    curr = node
    lst = []
    while curr:
        node = curr.data
        lst.append(str(node))
        curr = curr.next
    lst.append('None')

    return ' -> '.join(lst)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
