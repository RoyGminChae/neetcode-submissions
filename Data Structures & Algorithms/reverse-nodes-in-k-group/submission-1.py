# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prevNode = dummy
        currNode = head
        while self.isKRemaining(currNode, k):
            h, t, nextNode = self.reverse(currNode, k)

            prevNode.next = h
            t.next = nextNode

            prevNode = currNode
            currNode = t.next

        return dummy.next


    # reverse from currNode to k nodes
    # returns head and tail, nextNode
    # assumes left of head and right of tail is None
    def reverse(self, head, k):
        currNode = head
        prevNode = None

        i = 0
        while i < k:
            nextNode = currNode.next

            currNode.next = prevNode
            
            prevNode = currNode
            currNode = nextNode
            i += 1

        newHead = prevNode
        newTail = head

        return newHead, newTail, currNode 

    # including currNode is there k nodes left?
    # handles when head is None
    def isKRemaining(self, head, k):
        curr = head
        count = 0
        while curr:
            count += 1
            
            if count >= k:
                return True

            curr = curr.next
            
        return False
        

