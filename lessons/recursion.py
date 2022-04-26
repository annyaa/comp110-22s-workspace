from __future__ import annotations

from typing import Optional


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


# The following initially seems to be the most intuitive way to solve the problem of generating linked lists. A better way will be explored as we go on. 
def sum(node: Node) -> int:
    if node.next is None:  # base case
        return node.data
    else:
        return node.data + sum(node.next)  # node.next is the rest of the list since it keeps evaluating as long as we are not at base case wher node.next is None


def count(node: Node, current_count: int = 0) -> int:
    """Return number of nodes in a linked list."""
    if node.next is None:
        return current_count + 1
    else:
        return count(node.next, current_count + 1)


"""It is idiomatic to build linked lists from the bottom up."""
head: Node = Node(3, None)  # This is the last item in our list, this line of code is a constructor call. Head currently has a data object of 2 and a next object of None. 
head = Node(2, head)  # This first calls a constructor to make a new Node with 1 as data object and the node from line 24 as its next object. Head's value on the stack is then updated to refer to this newly created node. 
head = Node(1, head) 
print(sum(head))
print(count(head))