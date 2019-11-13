"""
Find is there is a connection between two components
"""


class QuickFind:
    """
    Quick Find: Eager Algorithm

    Data structure: Integer array id[] of size N
    Interpretation: p and q are connected iff(if and only if) they have the same
    id(array value)

    Find: Check if p and q have same entry. O(1)

    Union: To merge two components containing p and q, change all entries whose
    entry equal id[p] to id[q]. Problem in case where we have large array and there
    are too many components to change. O(n)

    N union commands on N objects will O(n^2)

    Defects:
    Union is too expensive(N array access)
    Trees are flat, but too expensive to keep them flat
    """

    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def connected(self, p, q) -> bool:
        try:
            return self.ids[p] == self.ids[q]
        except:
            print("Exception while checking for connection!")

    def union(self, p, q) -> None:
        if not self.connected(p, q):
            org_p = self.ids[p]
            q_val = self.ids[q]
            for i, elem in enumerate(self.ids):
                if elem == org_p:
                    self.ids[i] = q_val


class QuickUnion:
    """
    Quick Union:

    Data structure: Integer array id[] of size N
    Interpretation: id[i]
    Root of i is id[id[id[...id[i]...]]]

    Find: Check if p and q have root O(N)

    Union(p,q): Make the root of p as the child of root of q. O(N)
    Includes cost of finding root

    Defects:
    Trees can get tall
    Find can get too expensive

    """

    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def root(self, p):
        if p != self.ids[p]:
            return self.root(self.ids[p])
        return p

    def connected(self, p, q) -> bool:
        """Check if root od p is same as root of q"""
        try:
            return self.root(self.ids[p]) == self.root(self.ids[q])
        except:
            print("Exception while checking for connection!")

    def union(self, p, q) -> None:
        p_root = self.root(p)
        q_root = self.root(q)
        self.ids[p_root] = q_root


class WeightedQuickFind:
    """
    Weighted Quick Union algorithm:
    - Modify quick union to avoid tall trees
    - Keep track of size of each tree(number of objects)
    - Balancing by linking to root of smaller tree to the larger tree.

    Extra data structure sz to keep count of number of objects in a tree
    rooted at i

    Find: Same logic as above. Time taken proportional to depth of p and q.
    O(logN)

    Union: Takes O(logN), this includes finding root

    Proposition: Depth of any node is at most lg N
    """
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.sz = [1]*n
        self.largest = [i for i in range(n)]

    def root(self, p):
        if p != self.ids[p]:
            return self.root(self.ids[p])
        return p

    def remove(self, p):
        self.union(p, p+1)

    def successor(self, p):
        self.find_largest(p+1)

    def connected(self, p, q) -> bool:
        """Check if root od p is same as root of q"""
        try:
            return self.root(self.ids[p]) == self.root(self.ids[q])
        except:
            print("Exception while checking for connection!")

    def find_largest(self, p) -> int:
        return self.largest[self.root(p)]

    def union(self, p, q) -> None:
        p_root = self.root(p)
        q_root = self.root(q)
        q_largest = self.largest[q_root]
        p_largest = self.largest[p_root]
        if p_root == q_root:
            return
        if self.sz[p_root] > self.sz[q_root]:
            self.ids[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
            if q_largest > p_largest:
                self.largest[p_root] = q_largest
        else:
            self.ids[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
            if p_largest > q_largest:
                self.largest[q_root] = p_largest



class WQUPC:
    """
    Weight Quick Find with path compression

    Make root of all the nodes in the path of finding root of p, lets say q as
    q.

    Linear time algorithm  for M operations on N objects ?
    In theory not linear time: N + Mlg*N (lg*N: Number of time to take logs to
    get N)
    In practice linear time

    10^9 unions with 10^9 objects
    - WQUPC reduces from 30 years to 6 seconds.
    """



q = QuickFind(10)
q.connected(1, 4)
q.union(1, 2)
q.union(7, 8)
q.union(7, 9)
q.union(3, 4)
q.union(0, 5)
q.union(5, 6)
print(q.ids)

q = QuickUnion(10)
q.connected(1, 4)
q.union(1, 2)
q.union(7, 8)
q.union(7, 9)
q.union(3, 4)
q.union(0, 5)
q.union(5, 6)
print(q.ids)

print()
q = WeightedQuickFind(10)
q.connected(1, 4)
q.union(1, 2)
print(q.ids)
print(q.sz)
print(q.largest)

q.union(7, 8)
q.union(7, 9)
q.union(3, 4)
q.union(0, 5)
q.union(5, 6)
print(q.ids)
print(q.sz)
print(q.largest)
