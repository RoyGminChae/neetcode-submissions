# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        diameter = self.depth(root.left) + self.depth(root.right)
        diameterLeft = self.diameterOfBinaryTree(root.left)
        diameterRight = self.diameterOfBinaryTree(root.right)
        return max(diameter, diameterLeft, diameterRight)
    
    def depth(self, node):
        if node is None:
            return 0

        return 1 + max(self.depth(node.left), self.depth(node.right))
