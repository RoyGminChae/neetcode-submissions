class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        #imaginery boundaries for out of bounds 
        firstLeftShorter = [-1] * n
        firstRightShorter = [n] * n

        leftStack = [] # store indexes
        for i in range(len(heights) - 1, -1, -1):
            while leftStack and heights[leftStack[-1]] > heights[i]:
                firstLeftShorter[leftStack.pop()] = i
            leftStack.append(i)

        rightStack = []
        for i in range(len(heights)):
            while rightStack and heights[rightStack[-1]] > heights[i]:
                firstRightShorter[rightStack.pop()] = i
            rightStack.append(i)
        
        res = 0
        for i in range(len(heights)):
            area = heights[i] * (firstRightShorter[i] - firstLeftShorter[i] - 1)
            res = max(res, area) 
    

        return res
        


