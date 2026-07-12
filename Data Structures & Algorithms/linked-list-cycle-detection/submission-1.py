# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()

        def dfs(node):
            if node is None:
                return False

            if node in visited:
                return True
            
            visited.add(node)
            return dfs(node.next)

        return dfs(head)


