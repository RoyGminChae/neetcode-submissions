# undirected graph DFS cycle detection

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        G = {i: [] for i in range(n)}
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        visited = set()
        def dfs(u, parent): # cycle detection for undirected graphs
            visited.add(u)
            for v in G[u]:
                if v == parent:
                    continue

                if v in visited:
                    return True

                if dfs(v, u):
                    return True

            return False

        if dfs(0, None):
            return False
        
        return len(visited) == n
