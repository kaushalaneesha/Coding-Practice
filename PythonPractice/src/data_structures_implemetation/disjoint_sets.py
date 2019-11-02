class Node:
    def __init__(self, data, set):
        self.data = data
        self.next = None
        self.set = set


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def make_set(val: int) -> LinkedList:
    new_set = LinkedList()
    node = Node(val, new_set)
    node.set = new_set
    new_set.head = node
    new_set.tail = node
    return new_set


def make_set_wu(val: int) -> LinkedList:
    new_set = make_set(val)
    new_set.size = 1
    return new_set


def find_set(val: Node) -> int:
    return val.set.head.data


def union_set(x: Node, y: Node) -> LinkedList:
    x_list = x.set
    y_list = y.set
    x_list.tail = y_list.head
    y_head = y_list.head
    while y_head:
        y_head.set = x_list
        y_head = y_head.next
    x_list.tail = y_list.tail
    return x_list


def union_set_wu(x: Node, y: Node) -> LinkedList:
    x_list = x.set
    y_list = y.set
    if x_list.size >= y_list.size:
        res = union_set(x, y)
    else:
        res = union_set(y, x)
    res.size = x_list.size + y_list.size
    return res


s = make_set(10)
s2 = make_set(20)
# print(find_set(Node(10, s)))
ll = union_set(s.head, s2.head)
print(ll.head.data)
print(ll.tail.data)

s = make_set_wu(10)
s2 = make_set_wu(20)
# print(find_set(Node(10, s)))
ll = union_set_wu(s.head, s2.head)
print(ll.head.data)
print(ll.tail.data)
