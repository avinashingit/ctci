from copy import deepcopy


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


start_node = Node(1)
start_node.next = Node(2)
start_node.next.next = Node(3)
start_node.next.next.next = Node(4)
start_node.next.next.next.next = Node(5)

node = deepcopy(start_node)
remove_val = 4

cptr = deepcopy(node)
while node.next is not None:
    if node.value == remove_val:
        cptr.next = node.next
        break
    else:
        node = node.next
        cptr = node

cptr.value
