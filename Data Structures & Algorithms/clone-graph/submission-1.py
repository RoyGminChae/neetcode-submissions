"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyOf = dict()

        def dfs(node):
            if node is None:
                return None
            
            if node in copyOf:
                return copyOf[node]

            copy = Node(node.val)
            copyOf[node] = copy
            for v in node.neighbors:
                copy.neighbors.append(dfs(v))
            
            return copy

        return dfs(node)

        
            