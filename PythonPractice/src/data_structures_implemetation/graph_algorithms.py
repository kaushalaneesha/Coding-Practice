"""
Implementation of graph algorithms.
"""
import collections
import queue
from typing import List, Set


class Graph:
    def __init__(self):
        self.vertices = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.vertices[u].append(v)

    def breadth_first_search(self, source: int):
        """
        Assumption: All vertices are connected to the source
        """
        if not self.vertices or len(self.vertices[source]) == 0:
            print("Source not found in graph")
            return
        visited = set()
        traversal_queue = queue.Queue()
        traversal_queue.put(source)
        visited.add(source)
        while not traversal_queue.empty():
            elem = traversal_queue.get()
            print(elem)
            for e in self.vertices[elem]:
                if not visited.__contains__(e):
                    traversal_queue.put(e)
            visited.add(elem)

    def depth_first_search(self, source: int) -> List[int]:
        if not self.vertices or len(self.vertices[source]) == 0:
            print("Source not found in graph")
            return []
        visited = set()
        res = []
        for vertex in self.vertices:
            if not visited.__contains__(vertex):
                depth_first_search_util(g, vertex, visited, res)
        return res

    def topological_sort(self, source: int) -> collections.deque:
        """
        Logic is same as DFS, but we want result in reverse.
        For this we use deque here ( which internally uses linked list ) to
        add element at the start of the array
        :param source:
        :return:
        """
        if not self.vertices or len(self.vertices[source]) == 0:
            print("Source not found in graph")
            return collections.deque()
        res = collections.deque()
        visited = set()
        for vertex in self.vertices:
            if not visited.__contains__(vertex):
                topological_utils(g, vertex, visited, res)
        return res

def topological_utils(g, vertex, visited, res):
    for elem in g.vertices[vertex]:
        if not visited.__contains__(elem):
            topological_utils(g, elem, visited, res)
    res.appendleft(vertex)
    visited.add(vertex)


def depth_first_search_util(g: Graph, vertex: int, visited: Set[int], res: List[int]):
    for elem in g.vertices[vertex]:
        if not visited.__contains__(elem):
            depth_first_search_util(g, elem, visited, res)
    res.append(vertex)
    visited.add(vertex)


g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(2, 5)
g.add_edge(8, 3)
print(g.vertices)
g.breadth_first_search(1)
print("-------------------------------")
print(g.depth_first_search(1))
print(g.topological_sort(1))


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(4, 3)
g.add_edge(2, 3)
print(g.vertices)
g.breadth_first_search(1)
