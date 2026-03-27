from trash.preloaded import Node

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if not head:
        return None

    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
