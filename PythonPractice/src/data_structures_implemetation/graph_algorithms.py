"""
Implementation of breadth first search for a directed graph
"""
import collections
import queue
from typing import List


class Graph:
    def __init__(self):
        self.vertices = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.vertices[u].append(v)

    def breadth_first_search(self, source: int):
        visited = set()
        traversal_queue = queue.Queue()
        if not self.vertices:
            print("Nothing in the graph")
            return
        else:
            traversal_queue.put(source)
            visited.add(source)
            while traversal_queue:
                elem = traversal_queue.get()
                print(elem)
                for e in self.vertices[elem]:
                    if not visited.__contains__(e):
                        traversal_queue.put(e)
                visited.add(elem)


g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(2, 5)
print(g.vertices)
print(g.breadth_first_search(1))
