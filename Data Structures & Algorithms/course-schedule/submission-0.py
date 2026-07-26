from collections import defaultdict

class Solution:
    # topo sort cycle detection problem 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = {i: [] for i in range(numCourses)}
        
        for next, prev in prerequisites:
            G[prev].append(next)
        
        # detect cycle algorithm
        visitStatus = defaultdict(int) # 0, 1, 2
        def dfs(u): 
            if visitStatus[u] == 2: # already explored
                return False
            
            if visitStatus[u] == 1: # cycle detected
                return True

            visitStatus[u] = 1
            for v in G[u]:
                if dfs(v):
                    return True
            visitStatus[u] = 2
            
            return False
        
        for u in G:
            if dfs(u):
                return False

        return True

