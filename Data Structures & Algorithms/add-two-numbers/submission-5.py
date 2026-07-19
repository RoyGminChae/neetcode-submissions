# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# use recursion if the operation of the current node depends on the node after it
# for this one, iteration is preferred
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy

        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10

            curr.next = ListNode(val % 10)
            
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            carry = val // 10

            curr.next = ListNode(val % 10)
            curr = curr.next
            l1 = l1.next

        while l2:
            val = l2.val + carry
            carry = val // 10

            curr.next = ListNode(val % 10)
            curr = curr.next
            l2 = l2.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next