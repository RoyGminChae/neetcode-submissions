# average cost for both operations are nearly constant

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    

    def find(self, u):
        currNode = u
        while currNode != self.parent[currNode]:
            self.parent[currNode] = self.parent[self.parent[currNode]] # path compression
            currNode = self.parent[currNode]
        
        return currNode
    
    
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)

        if root_u == root_v:
            return False
        
        if self.size[root_u] > self.size[root_v]: # tree depth optimization
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                count -= 1
        
        return count

        