def loop_size(node):
    step1 = node.next
    step2s = node.next.next

    while step1 != step2s:
        step1 = step1.next
        step2s = step2s.next.next

    loop_length = 1
    step2s = step2s.next

    while step1 != step2s:
        step2s = step2s.next
        loop_length += 1

    return loop_length
