class Solution:
    # prefix/postfix more optimzed
    def trap(self, heights: List[int]) -> int:
        prefix = [0 for _ in range(len(heights))] # contains height
        postfix = [0 for _ in range(len(heights))]

        for i in range(1, len(heights)):
            prefix[i] = max(prefix[i - 1], heights[i - 1])
        
        for i in range(len(heights) - 2, -1, -1):
            rightHighest = max(postfix[i + 1], heights[i + 1])
            postfix[i] = rightHighest

        res = 0
        for i in range(len(heights)):
            res += max(min(prefix[i], postfix[i]) - heights[i], 0)
    
        return res

            

