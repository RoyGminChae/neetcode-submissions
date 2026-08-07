class Solution:
    # prefix/postfix method
    def trap(self, heights: List[int]) -> int:
        prefix = [0 for _ in range(len(heights))] # contains height
        postfix = [0 for _ in range(len(heights))]

        leftHighest = 0
        for i in range(1, len(heights)):
            leftHighest = max(leftHighest, heights[i - 1])
            prefix[i] = leftHighest
        
        rightHighest = 0
        for i in range(len(heights) - 2, -1, -1):
            rightHighest = max(rightHighest, heights[i + 1])
            postfix[i] = rightHighest

        res = 0
        for i in range(len(heights)):
            res += max(min(prefix[i], postfix[i]) - heights[i], 0)
    
        return res

            

