# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

# CS330 heap solution
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, arr in enumerate(lists):
            heapq.heappush(minHeap, (arr.val, i)) # value, reference, which list
        
        dummy = ListNode()
        currNode = dummy
        while minHeap:
            val, i = heapq.heappop(minHeap)
            currNode.next = lists[i]
            currNode = currNode.next
            
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i))


        return dummy.next


        

