# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # def recurse(node, level):
        #     if node is None:
        #         return 0
            
        #     if node.left is None and node.right is None:
        #         return level

        #     if node.left is None:
        #         return recurse(node.right, level + 1)

        #     if node.right is None:
        #         return recurse(node.left, level + 1)

        #     return max(recurse(node.left, level + 1), recurse(node.right, level + 1))
    
        # return recurse(root, 1)

