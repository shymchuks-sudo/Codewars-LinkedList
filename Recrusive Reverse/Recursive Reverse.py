from trash.preloaded import Node

def reverse(head):
    # your code goes here.
    if not head or not head.next:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
