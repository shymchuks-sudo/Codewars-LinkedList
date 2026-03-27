from trash.preloaded import Node

def swap_pairs(head):
    if not head:
        return head

    node = Node(0)
    node.next = head

    prev = node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first

        prev.next = second
        prev = first

    return node.next
