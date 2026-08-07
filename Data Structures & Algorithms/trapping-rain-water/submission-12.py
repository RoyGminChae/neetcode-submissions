class Solution:
    # two pointer 
    def trap(self, height: List[int]) -> int:
        left, right = 1, len(height) - 2
        
        leftMax = height[0]
        rightMax = height[-1]

        res = 0
        while left <= right:
            if leftMax < rightMax:
                water = max(leftMax - height[left], 0)
                leftMax = max(leftMax, height[left])
                res += water
                left += 1
            else:  
                water = max(rightMax - height[right], 0)
                rightMax = max(rightMax, height[right])
                res += water
                right -= 1
        
        return res