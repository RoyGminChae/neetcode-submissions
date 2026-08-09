from collections import deque

class Solution:
    # monotonic decreasing queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        right = 0
        res = []
        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            right += 1
                
            if queue[0] < left:
                queue.popleft()
            
            if (right - left + 1) > k:
                res.append(nums[queue[0]])
                left += 1
        
        return res
                





            
