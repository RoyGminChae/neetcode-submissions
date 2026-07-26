from collections import defaultdict

# DFS implementation of topological sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {i: [] for i in range(numCourses)}
        for u, v in prerequisites: # already reversed
            G[u].append(v)
        
        res = []

        status = defaultdict(int) # 0, 1, 2
        def dfs(u): # cycle detection
            if status[u] == 1:
                return True
            
            if status[u] == 2:
                return False

            status[u] = 1 # visiting
            for v in G[u]:
                if dfs(v):
                    return True
            status[u] = 2
            res.append(u)
            
            return False

        for u in G:
            if dfs(u): # cycle is detected
                return []
        
        return res


