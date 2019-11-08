"""
Find is there is a connection between two components
"""

# Quick Find: Eager Algorithm
"""
Data structure: Integer array id[] of size N 
Interpretation: p and q are connected iff(if and only if) they have the same 
id(array value) 

Find: Check if p and q have same entry. O(1)

Union: To merge two components containing p and q, change all entries whose 
entry equal id[p] to id[q]. Problem in case where we have large array and there
are too many components to change. O(n) 

N union commands on N objects will O(n^2)
"""


class QuickFind:
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


q = QuickFind(10)
q.connected(1, 4)
q.union(1, 2)
q.union(7, 8)
q.union(7, 9)
q.union(3, 4)
q.union(0, 5)
q.union(5, 6)
print(q.ids)
