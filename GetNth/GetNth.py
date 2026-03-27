from trash.preloaded import Node

def get_nth(node, index):
    '''
    >>> linked_list = Node(1, Node(2, Node(3, None)))
    >>> get_nth(linked_list, 0).data
    1
    >>> get_nth(linked_list, 1).data
    2
    >>> get_nth(linked_list, 2).data
    3
    '''
    if not isinstance(node, Node):
        raise ValueError("None linked list should throw error.")

    indx_max = -1
    while node:
        indx_max += 1
        if indx_max == index:
            return node
        node = node.next
    raise IndexError("Invalid index value should throw error.")

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
