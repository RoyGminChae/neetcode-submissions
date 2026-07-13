# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, maxVal):
            nonlocal count

            if root is None:
                return 
            
            if root.val >= maxVal:
                count += 1
            
            dfs(root.left, max(root.val, maxVal))
            dfs(root.right, max(root.val, maxVal))

        dfs(root, root.val)
        return count
            
