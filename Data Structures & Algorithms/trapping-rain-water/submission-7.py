class Solution:
    # two pointer
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxLeft = heights[left]
        maxRight = heights[right]
        
        res = 0

        while left < right: # come back here
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, heights[left])
                res += maxLeft - heights[left]
            else:
                right -= 1
                maxRight = max(maxRight, heights[right])
                res += maxRight - heights[right]

        return res
