class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            largestArea = max(largestArea, area)
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        
        return largestArea