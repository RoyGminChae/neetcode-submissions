# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def recurse(node, n):
            if node is None:
                return None
            
            node.next = recurse(node.next, n)
            n[0] -= 1
            if n[0] == 0:
                return node.next
            
            return node

        n = [n]
        return recurse(head, n)
