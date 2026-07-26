# Kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return []

        currSum = 0
        res = nums[0]
        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            res = max(res, currSum)
        
        return res