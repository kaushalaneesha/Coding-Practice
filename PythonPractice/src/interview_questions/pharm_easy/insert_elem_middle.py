"""
Insert element at the middle of a circular linked list
"""


class Node:
    """
    Node of a linked list
    """

    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class CircularLinkedList:

    def __init__(self, h: Node):
        self.head = h
        self.last = h
        if h:
            self.head.next = h
            self.last.next = h

    def append(self, elem):
        new_node = Node(elem)
        new_node.next = self.head
        self.last.next = new_node
        self.last = new_node

    def insert_elem_at_middle(self, elem):
        if not self.head:
            self.head = Node(elem)
            self.head.next = self.head
            return
        fast = self.head
        slow = self.head
        while fast.next != self.head and fast.next.next != self.head:
            print(slow.val)
            slow = slow.next
            fast = fast.next.next

        # Add new node
        new_node = Node(elem)
        new_node.next = slow.next
        slow.next = new_node
        if new_node.next == head:
            # update the last pointer as well
            self.last = new_node

    def print(self):
        if not self.head:
            return
        print(self.head.val)
        h = self.head.next
        while h != self.head:
            print(h.val)
            h = h.next


# Test case
head = Node(10)
l = CircularLinkedList(head)
l.append(2)
l.append(3)
l.append(4)
l.print()
l.insert_elem_at_middle(6)
l.print()
l.insert_elem_at_middle(18)
l.print()
l.insert_elem_at_middle(20)
l.print()


head = None
l = CircularLinkedList(head)
l.print()
l.insert_elem_at_middle(6)
l.print()



