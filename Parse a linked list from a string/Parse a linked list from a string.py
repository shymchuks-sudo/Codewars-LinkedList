from trash.preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(' -> ')
    curr = None
    for part in parts[::-1]:
        try:
            part = int(part)
        except ValueError:
            continue
        node = Node(part, curr)
        curr = node
    return curr
