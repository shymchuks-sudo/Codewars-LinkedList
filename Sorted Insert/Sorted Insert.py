from trash.preloaded import Node

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    node = Node(data)
    if not head or data < head.data:
        node.next = head
        return node

    curr = head
    while curr.next and curr.next.data < data:
        curr = curr.next
    node.next = curr.next
    curr.next = node
    return head
