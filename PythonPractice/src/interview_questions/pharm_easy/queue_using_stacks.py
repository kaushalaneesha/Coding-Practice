"""
Implement queue functionality using stacks
"""


class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        pass

    def enqueue(self, elem):
        """
        Add an element to the queue
        :return: None
        """
        self.stack1.append(elem)

    def dequeue(self):
        """
        Remove and return the first added or oldest element from the queue
        :return:
        """
        len_stack1 = len(self.stack1)
        if len_stack1 == 0:
            print("queue is empty!")
            return -1
        elif len_stack1 == 1:
            return self.stack1.pop()
        else:
            for _ in range(len_stack1 - 1):
                elem = self.stack1.pop()
                self.stack2.append(elem)
            res = self.stack1.pop()
            while self.stack2:
                elem = self.stack2.pop()
                self.stack1.append(elem)
            return res

    def size(self):
        """
        Returns the size of queue
        :return: int
        """
        return len(self.stack1)

    def is_empty(self):
        """
        Tells whether the queue is empty
        :return:
        """
        return not self.stack1

    def pick(self):
        """
        Returns the first element from the queue. This function doesn't delete the element from the queue
        :return:
        """
        len_stack1 = len(self.stack1)
        if len_stack1 == 0:
            print("queue is empty!")
            return -1
        elif len_stack1 == 1:
            return self.stack1.pop()
        else:
            for i in range(len_stack1 - 1):
                elem = self.stack1.pop()
                self.stack2.append(elem)
            res = self.stack1[0]
            while self.stack2:
                elem = self.stack2.pop()
                self.stack1.append(elem)
            return res


# test
q = Queue()
q.enqueue(2)
q.enqueue(3)
print("Queue is_empty: {}".format(q.is_empty()))
print("Queue size: {}".format(q.size()))
q.enqueue(4)
print("Queue element: {}".format(q.dequeue()))
q.enqueue(5)

print("Queue size: {}".format(q.size()))
print("Queue pick: {}".format(q.pick()))
print("Queue size: {}".format(q.size()))
print("Queue pick: {}".format(q.pick()))
print("Queue element: {}".format(q.dequeue()))
print("Queue is_empty: {}".format(q.is_empty()))
print("Queue element: {}".format(q.dequeue()))
print("Queue element: {}".format(q.dequeue()))
print("Queue is_empty: {}".format(q.is_empty()))
print("Queue size: {}".format(q.size()))
print("Queue size: {}".format(q.size()))
print("Queue pick: {}".format(q.pick()))

