# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = dummy # this makes it first middle node for even list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        head2 = slow.next
        slow.next = None

        prevNode = None
        currNode = head2
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        head2 = prevNode

        first = head
        second = head2

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2




