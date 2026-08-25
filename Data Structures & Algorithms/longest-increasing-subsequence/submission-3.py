# end in i dp version bottom-up
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
 
        for i in range(len(nums)):
            LIS = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[j])
            
            dp[i] = LIS

        return max(dp)

        