# fits perfectly into DSU

class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.size = {i: 1 for i in range(1, n + 1)}

    
    def find(self, u):
        curr = u
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        
        return curr


    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

